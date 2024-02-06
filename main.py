import json
import time

from CompanyHouseConnector import CompaniesHouseConnector, CompanyCollection

if __name__ == '__main__':

    company_collection = CompanyCollection()
    company_collection.read_from_csv("data/2024-01-30_-_Worker_and_Temporary_Worker.csv")

    company_connector = CompaniesHouseConnector()
    count = 0
    for company in company_collection.get_companies():
        company_name = company.get("name", "")
        print(f'Company: {company_name}')
        result = company_connector.search_companies(company_name)
        if result is None:
            continue
        if len(result["items"]) > 0:
            # Fix
            company_number = result["items"][0]['company_number']
            print(company_number)
            result = company_connector.get_company_profile(company_number)
            print(json.dumps(result, indent=4, sort_keys=True))
        if count >= 2:
            break
        count = count + 1
        time.sleep(3)
