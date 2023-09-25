package edikgoose.app_kotlin.controller

import edikgoose.app_kotlin.service.BaseConverterService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController

@RestController
class BaseConverterController(
    @Autowired val baseConverterService: BaseConverterService
) {
    @GetMapping("convert")
    fun sum(@RequestParam(name = "value") value: Int, @RequestParam(name = "base") base: Int): String {
        return baseConverterService.convert(value, base)
    }
}
