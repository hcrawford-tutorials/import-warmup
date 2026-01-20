def print_report(portfolio: list[dict]) -> None:
    total = calculate_portfolio_value(portfolio)
    print(f"PORTFOLIO SUMMARY\nPortfolio Name: {portfolio["name"]}")
    print("--------------------")
    print(f"Number of assets: {len{portfolio["assets"]}}")
    print(f"Total value: ${total:,.2f}")

def calculate_portfolio_value(portfolio: dict) -> float:
    total = 0
    for asset in portfolio["assets"]:
        total += calculate_asset_value(asset)
    return total