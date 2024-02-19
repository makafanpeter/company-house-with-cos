import time
from datetime import datetime

from CompanyHouseConnector import CompaniesHouseConnector, CompanyCollection, CompanyHouseHelper
from database import Database

if __name__ == '__main__':

    company_collection = CompanyCollection()
    company_collection.read_from_csv("data/2024-01-30_-_Worker_and_Temporary_Worker.csv")
    db = Database()

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
            current_company = result["items"][0]
            company_number = current_company.get('company_number', None)
            if company_number is None:
                continue
            print(company_number)
            current_company = db.get_company_house_db()["Companies"].find_one({"company_number": company_number})
            if current_company is not None:
                continue
            result = company_connector.get_company_profile(company_number)
            if result is not None:
                current_company = {
                    "name": result.get("company_name", ""),
                    "company_number": result.get("company_number", ""),
                    "status": result.get("company_status", ""),
                    "jurisdiction": result.get("jurisdiction", ""),
                    "industries": [CompanyHouseHelper.get_sic_code_mapping(industry.strip()) for industry in
                                   result.get("sic_codes", [])],
                    "type_and_rating": company["type_and_rating"],
                    "route": company["route"],
                    "type": result.get("type", ""),
                    "address": {
                        "street": f'{result["registered_office_address"].get("address_line_1", "")} '
                                  f'{result["registered_office_address"].get("address_line_2", "")}',
                        "country": result["registered_office_address"].get("country", ""),
                        "city": result["registered_office_address"].get("locality", ""),
                        "post_code": result["registered_office_address"].get("postal_code", ""),
                        "region": result["registered_office_address"].get("region", ""),
                    }
                }
                date_str = result.get("date_of_creation")
                if date_str:
                    datetime_object = datetime.strptime(date_str, '%Y-%m-%d')
                    current_company["incorporated_on"] = datetime_object

                current_company["created_at"] = datetime.now()
                print(current_company)
                db.get_company_house_db()["Companies"].insert_one(current_company)
        time.sleep(3)
