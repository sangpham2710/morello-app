package com.example.morello.ui.login

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import com.example.morello.ui.theme.login.LoginScreen

@Composable
fun LoginRoute(
    viewModel: LoginViewModel,
    switchToSignIn: () -> Unit,
    switchToForgotPassword: () -> Unit,
    onGoogleLoginRequest: () -> Unit,
    onFacebookLoginRequest: () -> Unit,
    onLoginSuccess: () -> Unit,
    modifier: Modifier,
) {
    val uiState by viewModel.uiState.collectAsState()
    LoginScreen(
        uiState = uiState,
        onEmailChanged = viewModel::updateEmail,
        onPasswordChanged = viewModel::updatePassword,
        onLoginButtonClicked = viewModel::submitLogin,
        onForgotPasswordClicked = switchToForgotPassword,
        onRememberMeChanged = viewModel::updateRememberMeStatus,
        onShowPasswordChanged = viewModel::updatePasswordVisibility,
        onSignInClicked = switchToSignIn,
        onGoogleLoginClicked = onGoogleLoginRequest,
        onLoginSuccess = onLoginSuccess,
        modifier = modifier,
    )
}