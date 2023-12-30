package com.example.morello

import AuthorizedHomeRoute
import LoginRoute
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.ui.Modifier
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.compose.rememberNavController
import com.example.morello.ui.navigation.MorelloNavHost
import com.example.morello.ui.theme.MorelloTheme
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MorelloTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    val navController = rememberNavController()
                    val viewModelProvider = ViewModelProvider(this)
                    MorelloNavHost(
                        navController = navController,
                        startDestination = AuthorizedHomeRoute.routeWithArgs,
                        viewModelProvider = viewModelProvider,
                    )
                }
            }
        }
    }
}
