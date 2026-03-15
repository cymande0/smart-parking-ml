# Project Ideas & Future Features

## Weather Integration
- Weather conditions affect parking behavior:
  - Snow/frost → drivers less likely to leave (need to clear snow first)
  - Rain → drivers leave faster (don't want to get wet)
  - High temperature → more frequent short trips
- Data source: OpenWeatherMap API (free tier, 1000 calls/day)
- Features to add to spot score:
  - weather_factor — multiplier based on current conditions
  - temperature — affects probability model
  - precipitation — snow vs rain vs clear

## Spot Scoring Factors (planned)
- is_edge — spot next to curb (less door damage risk)
- neighbor_activity — how often neighbors move their cars
- weather_factor — current weather conditions
- time_of_day — rush hour vs quiet hours
- day_of_week — weekday vs weekend patterns