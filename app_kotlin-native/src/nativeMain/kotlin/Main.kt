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

val counts_by_val = MutableList(101) { 0 }
val sum_by_val = MutableList(101) { 0 }

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
            val throwRes = dice.doThrow()
            call.respondText("You throw D$sides. Result is $throwRes")

            if (sides in 0..100) {
                val curCounts = counts_by_val[sides]
                val curSums = sum_by_val[sides]

                counts_by_val[sides] = curCounts + 1
                sum_by_val[sides] = curSums + throwRes
            }
        }

        get("metrics") {
            val tagName = "dice_thrower_mean_throws"

            var response = ""
            response += "# HELP $tagName Results of dice throws from D2 to D100\n"
            response += "# TYPE $tagName gauge\n"
            (2..100).forEach {
                val mean = if (counts_by_val[it] == 0) 0 else sum_by_val[it] / counts_by_val[it]
                response += "$tagName{dice=\"D$it\"} $mean\n"
            }

            call.respondText(response)
        }
    }
}
