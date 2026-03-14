# Settings Functions

This document details various setting functions for configuring strategy backtest and trading environment.

---

## `set_universe()` - Set Stock Pool

```python
set_universe(security_list)
```

-   **Usage Scenario**: Backtest, trading module.
-   **Interface Description**: Used to set or update the list of securities (stocks, funds, convertible bonds, etc.) that the strategy will operate. In stock strategies, this function is mainly used to set the default security list for data acquisition functions such as `get_history()`.
-   **Parameters**:
    -   `security_list` (str or list[str]): Security code or list.
-   **Return**: `None`

---

## `set_benchmark()` - Set Benchmark

```python
set_benchmark(security)
```

-   **Usage Scenario**: Backtest, trading module.
-   **Interface Description**: Set the performance benchmark for the strategy. After setting, various risk indicators in the backtest report (such as Alpha, Beta, Sharpe ratio, etc.) will be calculated based on this benchmark.
-   **Notes**:
    -   This function can only be used in `initialize()` function.
    -   If not set, the system defaults to using CSI 300 Index (`000300.SS`) as benchmark.
-   **Parameters**:
    -   `security` (str): Code of stock, index, or ETF.
-   **Return**: `None`

---

## `set_commission()` - Set Commission

```python
set_commission(commission_ratio=0.0003, min_commission=5.0, type="STOCK")
```

-   **Usage Scenario**: Backtest module.
-   **Interface Description**: Set the simulated trading commission during backtest.
-   **Notes**:
    -   Total backtest fee = commission + handling fee.
    -   Commission = `commission_ratio` * transaction amount (minimum `min_commission`).
    -   Handling fee is calculated according to exchange standards (e.g., 0.00487%).
-   **Parameters**:
    -   `commission_ratio` (float): Commission rate, default is 0.03%.
    -   `min_commission` (float): Minimum commission per transaction, default is 5 yuan.
    -   `type` (str): Transaction type, supports "STOCK", "ETF", "LOF".
-   **Return**: `None`

---

## `set_slippage()` / `set_fixed_slippage()` - Set Slippage

Slippage is used to simulate the difference between transaction price and order price caused by market delay, liquidity, and other factors in real trading.

### `set_slippage()` - Proportional Slippage

```python
set_slippage(slippage=0.001)
```

-   **Interface Description**: Set a percentage as slippage.
-   **Calculation Formula**: `Transaction Price = Order Price ± Order Price * slippage / 2`
-   **Parameters**:
    -   `slippage` (float): Slippage ratio, default is 0.001 (i.e., 0.1%).

### `set_fixed_slippage()` - Fixed Slippage

```python
set_fixed_slippage(fixed_slippage=0.0)
```

-   **Interface Description**: Set a fixed price as slippage.
-   **Calculation Formula**: `Transaction Price = Order Price ± fixed_slippage / 2`

---

> 🔙 **Return**: [API Documentation Home](README.md)