import pytest
import records

from steps_manager import StepsManager

@pytest.fixture
def database():
    database = records.Database('sqlite://')
    database.query("create table steps ( step_text text )")
    database.query("insert into steps values ( 'Example step 0' )")
    database.query("insert into steps values ( 'Example step 1' )")
    database.query("insert into steps values ( 'Example step 2' )")
    yield database

def test_it_gets_steps_from_the_db(database):
    steps_manager = StepsManager(database)

    assert steps_manager.get_steps() == [
        'Example step 0',
        'Example step 1',
        'Example step 2',
    ]

def test_it_adds_step_to_the_db(database):
    steps_manager = StepsManager(database)

    steps_manager.add_step('Example step 3')

    assert steps_manager.get_steps() == [
        'Example step 0',
        'Example step 1',
        'Example step 2',
        'Example step 3',
    ]

def test_it_deletes_a_step_from_the_db(database):
    steps_manager = StepsManager(database)

    steps_manager.delete_step('Example step 1')

    assert steps_manager.get_steps() == [
        'Example step 0',
        'Example step 2',
    ]
