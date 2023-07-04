def countries_data(filter=None):
    # This is a placeholder for the actual data. In a real application, this could be a database query or an API call.
    data = [
        {"name": "United States", "flag": "🇺🇸"},
        {"name": "Canada", "flag": "🇨🇦"},
        {"name": "United Kingdom", "flag": "🇬🇧"},
        {"name": "Australia", "flag": "🇦🇺"},
        {"name": "Germany", "flag": "🇩🇪"},
        # Add more countries as needed...
    ]

    if filter:
        data = [country for country in data if filter.lower() in country["name"].lower()]

    return data