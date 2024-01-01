package com.example.morello.data_layer.data_sources.data_types.groups

import com.fasterxml.jackson.annotation.JsonProperty

data class Group(
    @JsonProperty("id") val id: Int,
    @JsonProperty("name") val name: String,
    @JsonProperty("description") val description: String,
    @JsonProperty("is_leader") val isLeader: Boolean,
)