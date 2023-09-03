package com.example

import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.html.*
import io.ktor.server.netty.*
import io.ktor.server.routing.*
import kotlinx.html.body
import kotlinx.html.h1
import kotlinx.html.p
import java.text.SimpleDateFormat
import java.util.*

fun main() {
    embeddedServer(Netty, port = 8080, host = "0.0.0.0", module = Application::module)
        .start(wait = true)
}

fun getMoscowTime(): String {
    val moscowTimeZone = TimeZone.getTimeZone("Europe/Moscow")
    val dateFormat = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
    dateFormat.timeZone = moscowTimeZone
    val currentTime = Date()
    return dateFormat.format(currentTime)
}

fun Application.module() {
    routing {
        get("/") {
            val moscowTime = getMoscowTime()
            call.respondHtml {
                body {
                    h1 {
                        +"Current Time in Moscow:"
                    }
                    p {
                        +moscowTime
                    }
                }
            }
        }
    }
}
