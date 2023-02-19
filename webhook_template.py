{
    "Account_Settings": {
        "passphrase": "8j4tr38j8jfsvdap98g",
        "max_account_risk_per_trade": 1
    },
    "Order_Settings": {
        "binance_symbol": "BTCUSDT",
        "leverage": 1,
        "cash_bet_amount": 50,
        "order_type": "limit",
        "max_orderbook_depth": 10,
        "max_orderbook_price_offset": 1,
        "min_orderbook_price_offset": 0,
        "limit_forced_offset": 0
    },
    "Trade_Management": {
        "persistent_checks": 0,
        "position_boundaries": {
            "take_profit": 0.25,
            "stop_loss": 0.25
        },
        "trailing_stop_loss": {
            "trailing_stop_loss_percentage": -1,
            "trailing_stop_loss_activation_percentage": -1
        },
        "dca_entries": {
            "on_off": 0,
            "total_amount": 0,
            "opposite_boundary_percentage": 0.01,
            "number_of_steps": 2
        }
    },
    "Signals": {
        "Buy": {{plot("Buy")}},
        "Minimal_Buy": {{plot("Minimal Buy")}},
        "Strong_Buy": {{plot("Strong Buy")}},
        "Minimal_Strong_Buy": {{plot("Minimal Strong Buy")}},
        "Exit_Buy": {{plot("Exit Buy")}},
        "Sell": {{plot("Sell")}},
        "Minimal_Sell": {{plot("Minimal Sell")}},
        "Strong_Sell": {{plot("Strong Sell")}},
        "Minimal_Strong_Sell": {{plot("Minimal Strong Sell")}},
        "Exit_Sell": {{plot("Exit Sell")}},
        "Clear_Orders": 0
    }
}
