package com.example.morello.ui.navigation

import AuthorizedHomeRoute
import CreateExpenseRoute
import CreateGroupRoute
import CreateIncomeRoute
import ForgotPasswordCodeRoute
import ForgotPasswordRoute
import GroupMembersRoute
import GroupModeratorsRoute
import GroupOwnerHomeRoute
import GroupSettingsRoute
import HomeRoute
import LoginRoute
import OwnerGroupHomeRoute
import RegisterRoute
import SessionListRoute
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.NavGraphBuilder
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.navigation
import com.example.morello.ui.authorized_home.AuthorizedHomeRoute
import com.example.morello.ui.create_balance_entry.CreateExpenseRoute
import com.example.morello.ui.create_balance_entry.CreateExpenseViewModel
import com.example.morello.ui.create_balance_entry.CreateIncomeRoute
import com.example.morello.ui.create_group.CreateGroupRoute
import com.example.morello.ui.forgot_password.ForgotPasswordCodeValidationScreen
import com.example.morello.ui.forgot_password.ForgotPasswordEmailScreen
import com.example.morello.ui.login.LoginRoute
import com.example.morello.ui.owner_group.OwnerGroupRoute
import com.example.morello.ui.register.RegisterRoute
import com.example.morello.ui.balance_entry_list.BalanceEntryListRoute
import com.example.morello.ui.group_settings.GroupMembersRoute
import com.example.morello.ui.group_settings.GroupModeratorsRoute
import com.example.morello.ui.group_settings.GroupSettingsRoute
import com.example.morello.ui.session_list.SessionListRoute

fun NavGraphBuilder.ownerGroupHomeGraph(
    navController: NavHostController,
) {
    val graphRoute = OwnerGroupHomeRoute

    navigation(
        route = graphRoute.routeWithArgs,
        startDestination = GroupOwnerHomeRoute.routeWithArgs,
        arguments = graphRoute.args
    ) {
        composable(GroupOwnerHomeRoute.routeWithArgs) {
            val parentEntry = remember(it) {
                navController.getBackStackEntry(graphRoute.routeWithArgs)
            }
            OwnerGroupRoute(
                viewModel = hiltViewModel(parentEntry),
                onSettings = {
                    navController.navigate(GroupSettingsRoute.base)
                },
                onNewIncomeEntry = {
                    navController.navigate(CreateIncomeRoute.base)
                },
                onNewExpenseEntry = {
                    navController.navigate(CreateExpenseRoute.base)
                },
                onBalanceEntryList = {
                    navController.navigate(BalanceEntryListRoute.base)
                },
                onCollectSessionList = {
                    navController.navigate(SessionListRoute.base)
                },
                onBack = {
                    navController.popBackStack()
                })
        }
        composable(GroupSettingsRoute.routeWithArgs) {
            val parentEntry = remember(it) {
                navController.getBackStackEntry(graphRoute.routeWithArgs)
            }
            val groupId = parentEntry.arguments?.getInt(graphRoute.groupId)!!
            GroupSettingsRoute(
                viewModel = hiltViewModel(),
                onBack = { navController.popBackStack() },
                navToMembers = { navController.navigate(GroupMembersRoute.routeWithArgs) },
                navToModerators = { navController.navigate(GroupModeratorsRoute.routeWithArgs) }
            )
        }
        composable(GroupMembersRoute.routeWithArgs) {
            val parentEntry = remember(it) {
                navController.getBackStackEntry(graphRoute.routeWithArgs)
            }
            val groupId = parentEntry.arguments?.getInt(graphRoute.groupId)!!
            GroupMembersRoute(
                viewModel = hiltViewModel(),
                onBack = { navController.popBackStack() },
            )
        }
        composable(GroupModeratorsRoute.routeWithArgs) {
            val parentEntry = remember(it) {
                navController.getBackStackEntry(graphRoute.routeWithArgs)
            }
            val groupId = parentEntry.arguments?.getInt(graphRoute.groupId)!!
            GroupModeratorsRoute(
                viewModel = hiltViewModel(),
                onBack = { navController.popBackStack() },
            )
        }
        composable(
            CreateExpenseRoute.routeWithArgs
        ) {
            val parentEntry = remember(it) {
                navController.getBackStackEntry(graphRoute.routeWithArgs)
            }
            val groupId = parentEntry.arguments?.getInt(graphRoute.groupId)!!
            CreateExpenseRoute(
                groupId = groupId,
                viewModel = hiltViewModel(),
                onBack = {
                    navController.popBackStack()
                },
                modifier = Modifier.padding(10.dp)
            )
        }
        composable(CreateIncomeRoute.routeWithArgs) {
            val parentEntry = remember(it) {
                navController.getBackStackEntry(graphRoute.routeWithArgs)
            }
            val groupId = parentEntry.arguments?.getInt(graphRoute.groupId)!!
            CreateIncomeRoute(
                groupId = groupId,
                viewModel = hiltViewModel(),
                onBack = {
                    navController.popBackStack()
                },
                modifier = Modifier.padding(10.dp)
            )
        }
        composable(SessionListRoute.routeWithArgs) {
            val parentEntry = remember(it) {
                navController.getBackStackEntry(graphRoute.routeWithArgs)
            }
            SessionListRoute(
                viewModel = hiltViewModel(parentEntry),
                onSessionClicked = {},
                onCreateNewSession = {
                    navController.navigate(CreateIncomeRoute.base)
                },
                onBack = {
                    navController.popBackStack()
                },
            )
        }
        composable(BalanceEntryListRoute.routeWithArgs) {
            val parentEntry = remember(it) {
                navController.getBackStackEntry(graphRoute.routeWithArgs)
            }
            BalanceEntryListRoute(
                viewModel = hiltViewModel(parentEntry),
                onBalanceEntryClicked = {},
                onCreateNewBalanceEntry = {},
                onBack = {
                    navController.popBackStack()
                },
            )
        }
    }
}

fun NavGraphBuilder.authorizedHomeGraph(
    navController: NavHostController,
) {
    val graphRoute = AuthorizedHomeRoute

    navigation(
        startDestination = HomeRoute.routeWithArgs,
        route = graphRoute.routeWithArgs
    ) {
        ownerGroupHomeGraph(
            navController = navController,
        )
        composable(HomeRoute.routeWithArgs) {
            val parentEntry = remember(it) {
                navController.getBackStackEntry(graphRoute.routeWithArgs)
            }
            AuthorizedHomeRoute(
                viewModel = hiltViewModel(parentEntry),
                onCreateNewGroup = {
                    navController.navigate(CreateGroupRoute.base)
                },
                navigateToGroup = { groupId ->
                    navController.navigate("${OwnerGroupHomeRoute.base}/$groupId")
                }
            )
        }
        composable(CreateGroupRoute.routeWithArgs) {
            val parentEntry = remember(it) {
                navController.getBackStackEntry(graphRoute.routeWithArgs)
            }
            CreateGroupRoute(
                viewModel = hiltViewModel(parentEntry),
                onBack = {
                    navController.popBackStack()
                }
            )
        }
    }
}


@Composable
fun MorelloNavHost(
    navController: NavHostController,
    startDestination: String,
    modifier: Modifier = Modifier,
) {
    NavHost(
        navController = navController,
        startDestination = startDestination,
        modifier = modifier,
    ) {
        authorizedHomeGraph(
            navController = navController,
        )
        composable(LoginRoute.routeWithArgs) {
            LoginRoute(
                viewModel = hiltViewModel(),
                switchToSignIn = {
                    navController.navigate(RegisterRoute.base)
                },
                switchToForgotPassword = {
                    navController.navigate(ForgotPasswordRoute.base)
                },
                onGoogleLoginRequest = {
                    navController.navigate(LoginRoute.base)
                },
                onFacebookLoginRequest = {
                    navController.navigate(LoginRoute.base)
                },
                onLoginSuccess = {
                    navController.navigate(HomeRoute.base)
                },
                modifier = Modifier.padding(10.dp),
            )
        }
        composable(RegisterRoute.routeWithArgs) {
            RegisterRoute(
                viewModel = hiltViewModel(),
                switchToLogin = {
                    navController.navigate(LoginRoute.base)
                },
                modifier = Modifier.padding(10.dp),
            )
        }
        composable(ForgotPasswordRoute.routeWithArgs) {
            ForgotPasswordEmailScreen(
                email = "",
                onEmailChanged = {},
                onEmailSent = {
                    navController.navigate(ForgotPasswordCodeRoute.base)
                },
                onLoginClicked = { /*TODO*/ },
                onBack = { },
                modifier = Modifier.padding(10.dp),
            )
        }
        composable(ForgotPasswordCodeRoute.routeWithArgs) {
            ForgotPasswordCodeValidationScreen(
                email = "ltp@gmail.com",
                onBack = { /*TODO*/ })
        }
    }
}