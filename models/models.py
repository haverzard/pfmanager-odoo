# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Pegawai(models.Model):
    _name = 'pfmanager.pegawai'
    _description = ''

    nama = fields.Char()
    email = fields.Char()
    password = fields.Char()
    proyek_ids = fields.Many2many(
        'pfmanager.proyek', 'proyek_pegawai_rel', 'pegawai_id', 'proyek_id'
    )


class Proyek(models.Model):
    _name = 'pfmanager.proyek'
    _description = ''

    nama = fields.Char()
    pegawai_ids = fields.Many2many(
        'pfmanager.pegawai', 'proyek_pegawai_rel', 'proyek_id', 'pegawai_id'
    )
    peserta_id = fields.One2many(
        'pfmanager.peserta', 'proyek_id',
    )
    kebencanaan_id = fields.One2many(
        'pfmanager.kebencanaan', 'proyek_id',
    )
    assessment_id = fields.One2many(
        'pfmanager.assessment', 'proyek_id',
    )
    kegiatan_id = fields.One2many(
        'pfmanager.kegiatan', 'proyek_id',
    )


class Kebencanaan(models.Model):
    _name = 'pfmanager.kebencanaan'
    _description = ''

    rincian_kebencanaan = fields.Text()
    lokasi = fields.Char()
    waktu_observasi = fields.Datetime()
    proyek_id = fields.Many2one(
        'pfmanager.proyek'
    )


class Assessment(models.Model):
    _name = 'pfmanager.assessment'
    _description = ''

    kebutuhan = fields.Text()
    nama_narasumber = fields.Char()
    no_handphone = fields.Char()
    proyek_id = fields.Many2one(
        'pfmanager.proyek'
    )


class Kegiatan(models.Model):
    _name = 'pfmanager.kegiatan'
    _description = ''

    nama = fields.Char()
    waktu_mulai = fields.Datetime()
    waktu_akhir = fields.Datetime()
    proyek_id = fields.Many2one(
        'pfmanager.proyek'
    )
    resource_id = fields.One2many(
        'pfmanager.resource', 'kegiatan_id',
    )


class Resource(models.Model):
    _name = 'pfmanager.resource'
    _description = ''

    nama = fields.Char()
    beban_kerja = fields.Integer()
    biaya = fields.Integer()
    kegiatan_id = fields.Many2one(
        'pfmanager.kegiatan'
    )


class Peserta(models.Model):
    _name = 'pfmanager.peserta'
    _description = ''

    nama = fields.Char()
    tempat_tinggal = fields.Char()
    umur = fields.Integer()
    email = fields.Char()
    no_handphone = fields.Char()
    proyek_id = fields.Many2one(
        'pfmanager.proyek'
    )
    evaluasi_id = fields.One2many(
        'pfmanager.evaluasi', 'peserta_id',
    )
    progress_id = fields.One2many(
        'pfmanager.progress', 'peserta_id',
    )


class Progress(models.Model):
    _name = 'pfmanager.progress'
    _description = ''

    bulan_ke = fields.Integer()
    catatan = fields.Text()
    peserta_id = fields.Many2one(
        'pfmanager.peserta'
    )


class Evaluasi(models.Model):
    _name = 'pfmanager.evaluasi'
    _description = ''

    evaluasi = fields.Text()
    nilai_performansi = fields.Integer()
    peserta_id = fields.Many2one(
        'pfmanager.peserta'
    )
