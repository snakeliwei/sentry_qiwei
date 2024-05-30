# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms


class QiWeiOptionsForm(forms.Form):
    key = forms.CharField(
        max_length=255,
        help_text='QIWEI WEBHOOK KEY'
    )
