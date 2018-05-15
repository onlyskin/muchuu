import os, tempfile

import pytest
import records

from steps_manager import StepsManager

def test_it_gets_steps_from_the_db():
    db = records.Database('sqlite://')
    db.query("create table steps ( step_text text )")
    db.query("insert into steps values ( 'Example step 0' )")
    db.query("insert into steps values ( 'Example step 1' )")

    steps_manager = StepsManager(db)

    steps = steps_manager.get_steps()
    assert len(steps) == 2
    assert steps[0] == 'Example step 0'
    assert steps[1] == 'Example step 1'

def test_it_adds_step_to_the_db():
    db = records.Database('sqlite://')
    db.query("create table steps ( step_text text )")
    db.query("insert into steps values ( 'Example step 0' )")
    db.query("insert into steps values ( 'Example step 1' )")

    steps_manager = StepsManager(db)

    steps_manager.add_step('Example step 2')

    assert len(steps_manager.get_steps()) == 3
