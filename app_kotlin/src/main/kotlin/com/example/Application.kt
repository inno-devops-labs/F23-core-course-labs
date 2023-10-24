package com.example

import io.ktor.server.application.Application
import io.ktor.server.application.call
import io.ktor.server.engine.embeddedServer
import io.ktor.server.netty.Netty
import io.ktor.server.response.respondText
import io.ktor.server.routing.get
import io.ktor.server.routing.routing
import java.text.SimpleDateFormat
import java.util.Date
import java.util.TimeZone
import io.ktor.server.metrics.micrometer.*

fun main() {
    embeddedServer(Netty, port = 8080, host = "0.0.0.0", module = Application::module) {
        install(MicrometerMetrics)
    }.start(wait = true)
}

fun getMoscowTime(): String {
    val moscowTimeZone = TimeZone.getTimeZone("Europe/Moscow")
    val dateFormat = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
    dateFormat.timeZone = moscowTimeZone
    val currentTime = Date()
    return dateFormat.format(currentTime)
}

fun Application.module() {
    val appMicrometerRegistry = PrometheusMeterRegistry(PrometheusConfig.DEFAULT)
    install(MicrometerMetrics) {
        registry = appMicrometerRegistry
        distributionStatisticConfig = DistributionStatisticConfig.Builder()
            .percentilesHistogram(true)
            .maximumExpectedValue(Duration.ofSeconds(20).toNanos().toDouble())
            .serviceLevelObjectives(
                Duration.ofMillis(100).toNanos().toDouble(),
                Duration.ofMillis(500).toNanos().toDouble()
            )
            .build()
        meterBinders = listOf(
            JvmMemoryMetrics(),
            JvmGcMetrics(),
            ProcessorMetrics()
        )
    }
    routing {
        get("/") {
            val moscowTime = getMoscowTime()
            call.respondText("Current Time in Moscow:$moscowTime")
        }
        get("/metrics") {
            call.respond(appMicrometerRegistry.scrape())
        }
    }
}
