package com.example.morello.ui.login

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import com.example.morello.ui.theme.login.LoginScreen
import com.example.morello.ui.theme.login.LoginViewModel

@Composable
fun LoginRoute(
    viewModel: LoginViewModel,
    modifier: Modifier,
) {
    val uiState by viewModel.uiState.collectAsState()
    LoginScreen(
        uiState = uiState,
        onEmailChanged = { viewModel.updateEmail(it) },
        onPasswordChanged = { viewModel.updatePassword(it) },
        onLoginButtonClicked = { viewModel.submitLogin() },
        onForgotPasswordClicked = { /*TODO*/ },
        onRegisterClicked = { /*TODO*/ },
        onRememberMeChanged = { viewModel.setRememberMe(it) },
        onBack = { /*TODO*/ },
        onShowPasswordChanged = { /*TODO*/ },
        onGoogleLoginClicked = { /*TODO*/ },
        modifier = modifier,
    )
}