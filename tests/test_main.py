# import pytest
# from src.main import *


# data_OK = [
#     ("rouen", "paris"),
#     ("rouen", "versailles"),
#     ("rouen", "lyon"),
#     ("rouen", "dieppe"),
#     ("paris", "versailles"),
# ]


# data_KO = [
#     ("rouen", "lehavre"),
#     ("versailles", "versailles"),
#     ("versailles", "rouen"),
# ]


# @pytest.mark.parametrize("dep,dest", data_OK)
# def test_main_ok(dep, dest):

#     tu = (dep, dest)
#     assert modelize(tu) > 0


# @pytest.mark.parametrize("dep,dest", data_KO)
# def test_main_ko(dep, dest):

#     li = [("nex_york", "paris")]

#     tu = (dep, dest)
#     assert modelize(tu) < 0