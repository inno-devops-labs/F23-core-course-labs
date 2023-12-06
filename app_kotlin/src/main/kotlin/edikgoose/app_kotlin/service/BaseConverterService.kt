package edikgoose.app_kotlin.service

import edikgoose.app_kotlin.exception.IllegalBaseException
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import org.springframework.stereotype.Service
import java.lang.IllegalArgumentException

@Service
class BaseConverterService(
    val logger: Logger = LoggerFactory.getLogger(BaseConverterService::class.java)
) {
    fun convert(value: Int, base: Int): String {
        if (base < Character.MIN_RADIX || base > Character.MAX_RADIX) {
            throw IllegalBaseException()
        }
        try {
            logger.info("Value $value is converting to base $base")
            return value.toString(base)
        } catch (e: IllegalArgumentException) {
            logger.error("Error during converting value $value to base $base: $e")
            throw e
        }
    }
}
