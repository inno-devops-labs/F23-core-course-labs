package edikgoose.app_kotlin.service

import org.slf4j.Logger
import org.slf4j.LoggerFactory
import org.springframework.stereotype.Service
import java.io.BufferedReader
import java.io.File

@Service
class VisitsService(
    val logger: Logger = LoggerFactory.getLogger(BaseConverterService::class.java)
) {
    fun incrementNumberOfVisits() {
        val file = File(PATH)
        if (!file.exists()) {
            file.createNewFile()
        }

    }

    companion object {
        const val PATH = "/"
    }
}
