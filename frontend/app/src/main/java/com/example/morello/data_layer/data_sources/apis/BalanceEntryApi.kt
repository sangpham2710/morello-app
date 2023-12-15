package com.example.morello.data_layer.data_sources.apis

import com.example.morello.data_layer.data_sources.data_types.BalanceEntry
import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.DELETE
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.PUT
import retrofit2.http.Path

interface BalanceEntryApi {
    @GET("groups/{id}/entries")
    suspend fun getBalanceEntriesByGroupId(@Path("id") id: Int): Call<List<BalanceEntry>>

    @PUT("groups/{id}/entries/{entryId}")
    suspend fun updateBalanceEntryInGroup(
        @Path("id") id: Int,
        @Path("entryId") entryId: Int,
        @Body entry: BalanceEntry,
    ): Call<BalanceEntry>

    @POST("groups/{id}/entries")
    suspend fun addBalanceEntryToGroup(
        @Path("id") id: Int,
        @Body entry: BalanceEntry
    ): Call<BalanceEntry>

    @DELETE("groups/{id}/entries/{entryId}")
    suspend fun deleteBalanceEntryFromGroup(
        @Path("id") id: Int,
        @Path("entryId") entryId: Int
    ): Call<BalanceEntry>
}