package iu.devops.app_kotlin.service

import org.junit.jupiter.api.Test
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.test.context.TestConstructor
import kotlin.test.assertNotEquals

@SpringBootTest(
    classes = [
        TimeService::class
    ]
)
@TestConstructor(autowireMode = TestConstructor.AutowireMode.ALL)
class TimeServiceTest(
    private val timeService: TimeService
) {

    @Test
    fun `test time increase on refresh`() {
        val time1 = timeService.moscowTime()
        Thread.sleep(1000)
        val time2 = timeService.moscowTime()

        assertNotEquals(time1, time2)
    }
}
