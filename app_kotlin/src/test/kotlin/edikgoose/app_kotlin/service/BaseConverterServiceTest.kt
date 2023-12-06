package edikgoose.app_kotlin.service

import edikgoose.app_kotlin.exception.IllegalBaseException
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.assertDoesNotThrow
import org.junit.jupiter.api.assertThrows
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import java.lang.Character.MAX_RADIX
import kotlin.test.assertEquals

@SpringBootTest
class BaseConverterServiceTest(
    @Autowired val baseConverterService: BaseConverterService
) {

    @Test
    fun testConvert() {
        assertEquals(TEST_RESULT, baseConverterService.convert(TEST_VALUE, TEST_BASE))
    }

    @Test
    fun testConvertBaseMaxValue() {
        assertDoesNotThrow { baseConverterService.convert(TEST_VALUE, TEST_BASE_MAX_VALUE) }
    }

    @Test
    fun testConvertBaseMaxValueExceeded() {
        assertThrows<IllegalBaseException> { baseConverterService.convert(TEST_VALUE, TEST_BASE_MAX_VALUE + 1) }
    }

    companion object {
        const val TEST_VALUE = 150
        const val TEST_BASE = 2
        const val TEST_BASE_MAX_VALUE = MAX_RADIX
        const val TEST_RESULT = "10010110"
    }
}
