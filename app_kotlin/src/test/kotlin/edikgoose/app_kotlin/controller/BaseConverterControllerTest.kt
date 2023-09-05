package edikgoose.app_kotlin.controller

import edikgoose.app_kotlin.exception.IllegalBaseException
import edikgoose.app_kotlin.service.BaseConverterService
import org.junit.jupiter.api.Test
import org.mockito.ArgumentMatchers.anyInt
import org.mockito.Mockito.`when`
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest
import org.springframework.boot.test.mock.mockito.MockBean
import org.springframework.test.web.servlet.MockMvc
import org.springframework.test.web.servlet.ResultActions
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders
import org.springframework.test.web.servlet.result.MockMvcResultMatchers
import org.springframework.util.LinkedMultiValueMap

@AutoConfigureMockMvc
@WebMvcTest
class BaseConverterControllerTest(
    @Autowired val mockMvc: MockMvc,
) {
    @MockBean
    private lateinit var baseConverterService: BaseConverterService

    @Test
    fun testConvert() {
        `when`(baseConverterService.convert(anyInt(), anyInt())).thenReturn("150")

        val requestParams = LinkedMultiValueMap<String, String>()
        requestParams.add("value", "150")
        requestParams.add("base", "2")
        val perform: ResultActions = mockMvc.perform(
            MockMvcRequestBuilders.get("/convert").params(requestParams)
        )
        perform.andExpect(MockMvcResultMatchers.status().isOk)
    }

    @Test
    fun testConvertIllegalBase() {
        `when`(baseConverterService.convert(anyInt(), anyInt())).thenThrow(IllegalBaseException())

        val requestParams = LinkedMultiValueMap<String, String>()
        requestParams.add("value", "150")
        requestParams.add("base", "2")
        val perform: ResultActions = mockMvc.perform(
            MockMvcRequestBuilders.get("/convert").params(requestParams)
        )
        perform.andExpect(MockMvcResultMatchers.status().isBadRequest)
    }
}