from Booking_Functionality.bookings import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.check_the_selected_currency()
    bot.check_the_selected_search_query()
    bot.change_the_currency(currency="USD")
    bot.change_the_search_query(search="bookinggo")
    bot.choose_the_destination(destination="Islamabad")
