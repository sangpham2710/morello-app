package com.example.morello.ui.group_settings

import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.morello.data_layer.data_types.Group
import com.example.morello.data_layer.data_types.GroupDetail
import com.example.morello.data_layer.data_types.Member
import com.example.morello.data_layer.data_types.Moderator
import com.example.morello.data_layer.data_types.User
import com.example.morello.data_layer.repositories.GroupRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch
import java.time.OffsetDateTime
import javax.inject.Inject

data class GroupSettingsUiState(
    val group: GroupDetail,
    val members: List<Member>,
    val moderators: List<Moderator>
) {
    companion object {
        val empty = GroupSettingsUiState(
            group = GroupDetail(
                id = -1,
                name = "",
                description = "",
                createdAt = OffsetDateTime.now(),
                updatedAt = OffsetDateTime.now(),
                recentOpenSessions = emptyList(),
                recentBalanceEntries = emptyList(),
                leader = User(
                    id = -1,
                    name = "",
                    email = "",
                ),
            ),
            members = emptyList(),
            moderators = emptyList(),
        )
    }
}

@HiltViewModel
class GroupSettingsViewModel @Inject constructor(
    private val groupRepository: GroupRepository,
    savedStateHandle: SavedStateHandle
) : ViewModel() {
//    val groupId = savedStateHandle.get<Int>(GroupSettingsRoute.groupId)!!
    val groupId = 0
    private var _uiState = MutableStateFlow(GroupSettingsUiState.empty)
    val uiState = _uiState.asStateFlow()

    init {
        reload()
    }

    fun reload() {
        viewModelScope.launch {
            _uiState.update {
                it.copy(
                    group = groupRepository.getGroupDetail(groupId),
                    members = groupRepository.getMembers(groupId),
                    moderators = emptyList()
                )
            }
//            _uiState.value = GroupSettingsUiState(
//                group = GroupInfo(
//                    id = groupId,
//                    name = "Test Group",
//                    description = "This is a test group",
//                ),
//                members = listOf(
//                    Member(
//                        id = 123,
//                        name = "Member 1",
//                        isArchived = false,
//                        createdAt = OffsetDateTime.now(),
//                        updatedAt = OffsetDateTime.now()
//                    ),
//                    Member(
//                        id = 456,
//                        name = "Member 2",
//                        isArchived = false,
//                        createdAt = OffsetDateTime.now(),
//                        updatedAt = OffsetDateTime.now()
//                    )
//                ),
//                moderators = listOf(
//                    Moderator(
//                        id = 1,
//                        userId = 1234,
//                        userEmail = "mod1@email.com",
//                        createdAt = OffsetDateTime.now(),
//                        updatedAt = OffsetDateTime.now()
//                    ),
//                    Moderator(
//                        id = 2,
//                        userId = 5678,
//                        userEmail = "mod2@email.com",
//                        createdAt = OffsetDateTime.now(),
//                        updatedAt = OffsetDateTime.now()
//                    )
//                )
//            )
        }
    }
}
