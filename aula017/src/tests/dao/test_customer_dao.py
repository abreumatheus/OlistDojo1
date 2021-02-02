from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.customer_dao import CustomerDao
from src.models.customer import Customer
import pytest


class TestCustomerDao:
    def test_instance(self):
        customer_dao = CustomerDao()
        assert isinstance(customer_dao, CustomerDao)

    def test_save(self):
        customer = Customer('Um nome', 'Documento', '16999999999')
        customer_saved = CustomerDao().save(customer)

        assert customer_saved.id_ is not None
        CustomerDao().delete(customer_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            CustomerDao().save('customer')

    def test_read_by_id(self):
        customer = Customer('Um nome', 'Documento', '16999999999')
        customer_saved = CustomerDao().save(customer)
        customer_read = CustomerDao().read_by_id(customer_saved.id_)

        assert isinstance(customer_read, Customer)
        CustomerDao().delete(customer_read)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            CustomerDao().read_by_id('customer_saved.id_')

    def test_read_all(self):
        customer_read = CustomerDao().read_all()
        assert isinstance(customer_read, list)

    def test_delete(self):
        customer = Customer('Um nome', 'Documento', '16999999999')
        customer_saved = CustomerDao().save(customer)
        customer_read = CustomerDao().read_by_id(customer_saved.id_)
        CustomerDao().delete(customer_read)
        customer_read = CustomerDao().read_by_id(customer_saved.id_)

        assert customer_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            CustomerDao().delete('customer_read')
