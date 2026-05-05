def conversion_by_channel(df):
    return df.groupby('CampaignChannel')['Conversion'].mean()

def conversion_by_type(df):
    return df.groupby('CampaignType')['Conversion'].mean()

def conversion_by_platform(df):
    return df.groupby('AdvertisingPlatform')['Conversion'].mean()

def landing_page_conversion(df):
    return df.groupby('landing_page')['converted'].mean()