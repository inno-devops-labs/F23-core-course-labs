package edikgoose.app_kotlin.controller

import edikgoose.app_kotlin.service.BaseConverterService
import edikgoose.app_kotlin.service.VisitsService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController

@RestController
class BaseConverterController(
    @Autowired val baseConverterService: BaseConverterService,
    @Autowired val visitsService: VisitsService
) {
    @GetMapping("convert")
    fun sum(@RequestParam(name = "value") value: Int, @RequestParam(name = "base") base: Int): String {
        return baseConverterService.convert(value, base)
    }

    @GetMapping
    fun health(): String {
        return Constants.HEALTHY_ANSWER
    }

    @GetMapping("visits")
    fun visits(): String {
        return String()
    }
}


object Constants {
    const val HEALTHY_ANSWER = "healthy"
}
