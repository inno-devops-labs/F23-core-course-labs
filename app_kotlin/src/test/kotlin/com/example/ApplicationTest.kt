package com.example

import io.ktor.http.*
import io.ktor.server.testing.*
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.BeforeAll
import org.junit.jupiter.api.AfterAll
import org.junit.jupiter.api.TestInstance
import kotlin.test.assertEquals
import kotlin.test.assertTrue

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class KtorApplicationTest {

    private lateinit var server: TestApplicationEngine

    @BeforeAll
    fun setup() {
        server = createTestServer()
        server.start()
    }

    @AfterAll
    fun teardown() {
        server.stop(0, 0)
    }

    @Test
    fun testRoot() {
        with(server) {
            handleRequest(HttpMethod.Get, "/").response.let { response ->
                assertEquals(HttpStatusCode.OK, response.status())
                assertTrue(response.content!!.contains("Current Time in Moscow:"))
            }
        }
    }

    private fun createTestServer(): TestApplicationEngine {
        return TestApplicationEngine(createTestEnvironment {
            module { main() } // this is the module with the ApplicationKt.main() function
        })
    }
}
