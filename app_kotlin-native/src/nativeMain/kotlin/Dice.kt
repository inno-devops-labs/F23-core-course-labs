import kotlin.random.Random
import kotlin.random.nextInt

class Dice(
    val sides: Int
) {
    init {
        require(sides > 0) {
            "Amount of sides should be greater than zero"
        }
    }

    fun doThrow() = Random.nextInt(1..sides)
}