package ru.msidorskaya.lab1.controller

import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.ResponseBody
import java.io.File

@Controller
class PageCounterController {
    init {
        launchNumber = 1
        totalLaunchNumber = try {
            File(FILE_NAME).readText().toLong()
        } catch (ex: Exception) {
            0L // If the file is not created, or it contains unparseable Long, the count starts from 0
        }
    }

    @ResponseBody
    @GetMapping("/")
    fun getCurrentOpenNumber() =
        "Воу, с момента последнего рестарта приложения Вы открывали эту страницу уже $launchNumber раз!"
            .also {
                launchNumber += 1
            }

    @ResponseBody
    @GetMapping("/visits")
    fun getTotalVisitsCount(): String {
        totalLaunchNumber += 1

        val file = File(FILE_NAME)
        file.writeText(totalLaunchNumber.toString())

        return totalLaunchNumber.toString()
    }

    companion object {
        var launchNumber = 1
        var totalLaunchNumber = 0L

        private const val FILE_NAME = "visit-counter.txt"
    }
}
