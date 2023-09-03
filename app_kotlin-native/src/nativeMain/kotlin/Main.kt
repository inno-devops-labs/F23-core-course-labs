import io.ktor.server.application.*
import io.ktor.server.cio.*
import io.ktor.server.engine.*
import io.ktor.server.response.*
import io.ktor.server.routing.*

fun main() {
    embeddedServer(CIO, port = 8080, module = Application::myApplicationModule).start(wait = true)
}

fun Application.myApplicationModule() {
    routing {
        get("/") {
            if ("d" !in call.request.queryParameters) {
                call.respondText("Please provide the number of sides in \"d\" parameter")
                return@get
            }
            val sidesRaw: String = call.request.queryParameters["d"]!!
            val regEx = Regex("[0-9]+")
            if (regEx.matchEntire(sidesRaw) == null) {
                call.respondText("Please provide the correct number of sides")
                return@get
            }
            val sides = sidesRaw.toInt()
            val dice = Dice(sides)
            call.respondText("You throw D$sides. Result is${dice.doThrow()}")
        }
    }
}