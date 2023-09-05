import io.ktor.server.application.Application
import io.ktor.server.application.call
import io.ktor.server.cio.CIO
import io.ktor.server.engine.embeddedServer
import io.ktor.server.response.respondText
import io.ktor.server.routing.get
import io.ktor.server.routing.routing

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
