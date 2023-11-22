package edikgoose.app_kotlin.service

import org.springframework.stereotype.Service
import java.io.File

@Service
class VisitsService {
    fun incrementNumberOfVisits() {
        val file = File(FILE_PATH)

        if (!file.exists()) {
            file.parentFile.mkdirs()
            file.createNewFile()
            file.writeText("0")
            return
        }
        val currentCounter = file.readText().toInt()
        file.writeText((currentCounter + 1).toString())
    }

    fun getNumberOfVisits(): Int {
        val file = File(FILE_PATH)
        if (!file.exists()) {
            file.parentFile.mkdirs()
            file.createNewFile()
            file.writeText("0")
            return 0
        }
        return file.readText().toInt()
    }

    companion object {
        const val FILE_PATH = "./sources/visits"
    }
}
