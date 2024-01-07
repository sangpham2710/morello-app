package com.example.morello.ui.collect_session_detail

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.morello.data_layer.data_types.Currency
import com.example.morello.data_layer.repositories.CollectSessionRepository
import com.example.morello.data_layer.repositories.MemberRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import java.time.OffsetDateTime
import javax.inject.Inject

enum class State {
    Uninitialized,
    Idle,
    WaitingForResponse,
    Error,
}

enum class EntryState {
    Idle,
    WaitingForResponse,
}

data class CollectSessionDetailUiState(
    val name: String,
    val description: String,
    val totalAmount: Currency,
    val amountPerMember: Currency,
    val previewedMemberList: List<Entry>,
    val paidCount: Int,
    val unpaidCount: Int,
    val dueIn: OffsetDateTime,
) {
    data class Entry(
        val id: Int,
        val name: String,
        val paid: Boolean,
    )
}

@HiltViewModel
class CollectSessionDetailViewModel @Inject constructor(
    private val collectSessionRepository: CollectSessionRepository,
) : ViewModel() {
    var state by mutableStateOf(State.Uninitialized)
        private set
    var uiState: CollectSessionDetailUiState? by mutableStateOf(null)
        private set

    suspend fun init(groupId: Int, sessionId: Int) {
        val detail = collectSessionRepository.getCollectSession(groupId, sessionId)
        val memberStatuses = detail.memberStatuses

        state = State.Idle
        uiState = CollectSessionDetailUiState(
            name = detail.name,
            description = detail.description,
            dueIn = detail.due,
            amountPerMember = detail.paymentPerMember,
            totalAmount = detail.paymentPerMember * memberStatuses.size,
            paidCount = memberStatuses.count { it.status == "paid" },
            unpaidCount = memberStatuses.count { it.status == "unpaid" },
            previewedMemberList = memberStatuses.map {
                CollectSessionDetailUiState.Entry(
                    id = it.id,
                    name = it.name,
                    paid = it.status == "paid",
                )
            },
        )
    }

    fun updateMemberPaidStatus(groupId: Int, sessionId: Int, memberId: Int, paid: Boolean) {
        viewModelScope.launch {
            try {
                collectSessionRepository.updateCollectSessionEntryStatus(
                    groupId,
                    sessionId,
                    memberId,
                    paid
                )
                uiState = uiState?.copy(
                    previewedMemberList = uiState!!.previewedMemberList.map {
                        if (it.id == memberId) {
                            it.copy(paid = paid)
                        } else {
                            it
                        }
                    }
                )
            } catch (e: Exception) {
                state = State.Error
            }
        }
    }
}