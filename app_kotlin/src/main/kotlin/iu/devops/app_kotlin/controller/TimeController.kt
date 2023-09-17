package iu.devops.app_kotlin.controller

import io.github.oshai.kotlinlogging.KotlinLogging
import iu.devops.app_kotlin.service.TimeService
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController

@RestController("/")
class TimeController(
    private val timeService: TimeService
) {

    /**
     * @return text string that contains current time in "Europe/Moscow" timezone
     */
    @GetMapping
    fun time(): String = runCatching {
        timeService.moscowTime()
    }.onSuccess {
        logger.info { "Moscow time was sent" }
    }.onFailure {
        logger.error { it }
    }.getOrThrow()

    companion object {
        private val logger = KotlinLogging.logger { }
    }
}
