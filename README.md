# Eve Online LP Calculator

## Project Description
The **Eve Online LP Calculator** is a web application that allows users to explore all items available for purchase in the LP (Loyalty Point) stores of the universe of **EVE Online**.

The application helps players analyze which items are the most profitable to purchase by calculating the **ISK / LP ratio** and presenting the items ordered by profitability.

---

The project has been successfully deployed and is now live. You can access it at the following URL:

http://eve-bbewageuc4cvh4gm.italynorth-01.azurewebsites.net

Please visit the link to explore the full functionality and features of the application.

---
## Main Functionalities

### LP Store Overview
- Displays all in-game items available in LP stores
- Items are ordered by **profitability (ISK / LP ratio)**

### User Authentication
After authentication, users can:

- Select and add items to a **personal watchlist**
- Organize selected items into **custom tables**
- Move items between tables according to personal criteria

### Watchlist Management
- Create multiple tables for organizing items
- Move and group items based on the user's strategy
- For the convenience of players, a description can be added to each watchlist.

### Resource Cost Calculation
- Display all **required resources** needed to obtain selected items
- Calculate the **total cost** of purchasing those resources

---

## Planned Features (To Be Implemented)

### Inventory Check
After Character authorization via EVE SSO, the application will be able to:

- Check which resources the player already owns
- Display which resources **still need to be purchased**

---

## Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/TodorKav/eve_online.git
cd eve_online
pip install -r requirements.txt
python manage.py runserver
Database Setup
- python manage.py makemigrations
- python manage.py migrate
- Run the data fetching scripts located in:
eve/industry/db_fetching_scripts
Before running the scripts, carefully read:
scripts running sequence.md
located in the same folder.
Optionally, for some scripts that take longer to fetch data, alternative 
versions are provided that utilize Celery and Redis for improved performance.
Using Celery and Redis allow concurrent data fetching, 
which drastically reduces the time needed to fetch all data. 
However, it requires additional setup of Celery and Redis

⚠️ Important:
The data fetching process takes approximately 1.5 hours to complete.
Enabling concurrent fetching with Celery and Redis can reduce this time to around 20 minutes.