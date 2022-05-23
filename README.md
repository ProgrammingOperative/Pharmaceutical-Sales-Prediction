# Pharmaceutical-Sales-Prediction


# Business Understanding
Rossman Pharmaceuticals has multiple stores across several cities. Managers in individual stores rely on their years of experience as well as their personal judgment to forecast sales. The data team has however identified that factors such as promotions, competition, school and state holidays, seasonality, and locality as necessary for predicting the sales across the various stores.
The purpose of this project is to build and serve an end-to-end product that forecast sales in all their stores six weeks ahead of time to analysts in the finance team.



# Data
Files in the data include:
* train.csv - historical data including Sales
* test.csv - historical data excluding Sales, this is the data we will do the forecasting to
* sample_submission.csv - a sample submission file in the correct format
* store.csv - supplemental information about the stores



## Column Description
* Columns of the data are as described below:
* Id - an Id that represents a (Store, Date) duple within the test set
* Store - a unique Id for each store
* Sales - the turnover for any given day (this is what you are predicting)
* Customers - the number of customers on a given day
* Open - an indicator for whether the store was open: 0 = closed, 1 = open
* StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
* SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public schools
* StoreType - differentiates between 4 different store models: a, b, c, d
* Assortment - describes an assortment level: a = basic, b = extra, c = extended. Read more about assortment here
* CompetitionDistance - distance in meters to the nearest competitor store
* CompetitionOpenSince[Month/Year] - gives the approximate year and month of the time the nearest competitor was opened
* Promo - indicates whether a store is running a promo on that day
* Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
* Promo2Since[Year/Week] - describes the year and calendar week when the store started participating in Promo2
* PromoInterval - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store




# Installation




# ML Pipeline Design




# Skills Implemented In the Project
