import kotlin.test.Test
import kotlin.test.assertTrue

class DiceTest {
    @Test
    fun `test negative sides`() {
        var exceptionThrown = false
        try {
            Dice(-1)
        } catch (e: IllegalArgumentException) {
            exceptionThrown = true
        }

        assertTrue(exceptionThrown)
    }
}
