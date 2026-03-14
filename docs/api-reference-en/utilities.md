# Utility Functions API

This document details various auxiliary utility functions provided by the Ptrade platform, including logging, system interaction, communication, and permission management.

---

## Logging and Debugging

### `log()` - Log Recording

-   **Interface Description**: Print logs during strategy execution for debugging and monitoring. Supports different levels of log recording.
-   **Usage**:
    ```python
    log.debug("This is a debug message")
    log.info("This is an info message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    log.critical("This is a critical error message")
    ```
-   **Parameters**:
    -   `content`: Can be string, object, or any content that needs to be printed.
-   **Return**: `None`.

### `is_trade()` - Environment Check

-   **Interface Description**: Determine whether the current strategy is running in **trading** environment or **backtest** environment.
-   **Return**: `bool`. Returns `True` in trading environment, `False` in backtest environment.

### `check_limit()` - Limit Up/Down Status Check

-   **Interface Description**: Check the limit up/down status of specified securities on a specified date.
-   **Parameters**:
    -   `security` (str or list[str]): Single or multiple security codes.
    -   `query_date` (str, optional): Query date, format `YYYYMMDD`. Defaults to current date.
-   **Return**: `dict`. Key is security code, value is status code:
    -   `1`: Limit up
    -   `-1`: Limit down
    -   `2`: Touch limit up
    -   `-2`: Touch limit down
    -   `0`: No limit

---

## File and Path

### `create_dir()` - Create Directory

-   **Interface Description**: Create a new subdirectory under the research environment root directory.
-   **Notes**: Ptrade disables the `os` module, please use this function to create directories. Root directory is `/home/fly/notebook/`.
-   **Parameters**:
    -   `user_path` (str): Subdirectory path to create, such as `'my_data'` or `'my_data/daily'`.
-   **Return**: `None`.

### `get_research_path()` - Get Research Path

-   **Interface Description**: Get the root directory path of the research environment.
-   **Return**: String, root path of research environment (`/home/fly/notebook/`).

### `convert_position_from_csv()` - Load Position from CSV

-   **Usage Scenario**: Only available in backtest module.
-   **Interface Description**: Load initial position from CSV file for backtest.

---

> 🔙 **Return**: [API Documentation Home](README.md)