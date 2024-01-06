package com.example.morello.ui.create_balance_entry

import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Modifier
import kotlinx.coroutines.launch

@Composable
fun CreateIncomeRoute(
    groupId: Int,
    viewModel: CreateIncomeViewModel,
    onBack: () -> Unit,
    modifier: Modifier,
) {
    val uiState = viewModel.uiState
    LaunchedEffect(uiState.state) {
        if (uiState.state == State.Uninitialized) {
            viewModel.init(groupId)
        }
        if (uiState.state == State.Success) {
            viewModel.finish()
            onBack()
        }
    }
    CreateIncomeScreen(
        uiState = uiState,
        onBalanceChanged = viewModel::updateAmount,
        onNameChanged = viewModel::updateName,
        onDescriptionChanged = viewModel::updateDescription,
        onDateTimeChanged = viewModel::updateDateTime,
        onCreate = {
            viewModel.submit(groupId)
        },
        onSwitchToCreateNewEntry = viewModel::switchToCreateNewEntry,
        onSwitchToOpenCollectSession = viewModel::switchToCreateNewSession,
        onPaymentPerMemberChanged = viewModel::updateAmountPerMember,
        onStartDateTimeChanged = viewModel::updateStartDateTime,
        onEndDateTimeChanged = viewModel::updateEndDateTime,
        onMemberUpdated = viewModel::updateChosenMember,
        onConfirmGoBack = onBack,
        onDismissDateTimeError = viewModel::dismissDateTimeError,
        modifier = modifier,
    )
}
