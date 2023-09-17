package ru.msidorskaya.lab1

import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Test
import ru.msidorskaya.lab1.controller.PageCounterController

class PageCounterControllerTest {

    @Test
    fun `page counter returns int test`() {
        val response = PageCounterController().getCurrentOpenNumber()
        val (callNumber) = DEFAULT_MESSAGE_REGEXP.find(response)!!.destructured
        Assertions.assertDoesNotThrow({ callNumber.toInt() }, "Response $response is not parsable as Int")
    }

    @Test
    fun `page counter returns one on first opening`() {
        val response = PageCounterController().getCurrentOpenNumber()
        val (callNumber) = DEFAULT_MESSAGE_REGEXP.find(response)!!.destructured
        val expectedCallNumber = 1L
        Assertions.assertEquals(callNumber.toInt(), 1, "Page counter returned $response instead of $expectedCallNumber")
    }

    @Test
    fun `page counter increments responses on each call`() {
        val pageCounterController = PageCounterController()
        val actualResponses = (1..10).map { pageCounterController.getCurrentOpenNumber() }
        val expectedResponses = (1..10).map { "Воу, Вы открывали эту страницу уже $it раз!" }
        println(actualResponses)
        println(expectedResponses)
        Assertions.assertEquals(
            expectedResponses,
            actualResponses,
            "Actual responses $actualResponses doesn't match the expected responses: $expectedResponses"
        )
    }

    companion object {
        private val DEFAULT_MESSAGE_REGEXP = Regex("Воу, Вы открывали эту страницу уже (\\d+) раз!")
    }
}