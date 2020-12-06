# -*- coding: utf-8 -*-
from odoo import http


def middleware_check_attrs(req_data, attrs=[]):
    data = {}
    for attr in attrs:
        data[attr] = req_data.get(attr, None)
        if data[attr] is None:
            return http.Response("Require input `" + attr + "`", status=400), True
    return data, False


class PFManager(http.Controller):
    # @http.route('/', auth='public')
    # def index(self, **kw):
    #     return http.request.render('pfmanager.homepage', {
    #         'root': '/pfmanager',
    #     })

    @http.route('/login', auth='public', csrf=False, methods=['GET'])
    def login_page(self, **kw):
        return http.request.render('pfmanager.homepage', {
            'root': '/pfmanager',
        })

    @http.route('/login', auth='public', csrf=False, methods=['POST'])
    def login(self, db, email, password):
        http.request.session.authenticate(db, email, password)
        return 'Login success'

class Proyek(http.Controller):
    @http.route('/proyek/', auth='public', methods=['GET'])
    def daftar_proyek(self, **kw):
        return http.request.render('pfmanager.listing', {
            'root': '/pfmanager',
            'objects': http.request.env['pfmanager.proyek'].search([]),
        })

    @http.route('/proyek/', auth='public', csrf=False, methods=['POST'])
    def buat_proyek(self, **kw):
        data, err = middleware_check_attrs(
            kw, ['nama']
        )
        if err:
            return data
        http.request.env['pfmanager.proyek'].sudo().create(data)
        return http.Response("Successfully created", status=201)


    @http.route('/pfmanager/proyek/<model("pfmanager.proyek"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('pfmanager.object', {
            'object': obj
        })

    @http.route(
        '/proyek/<model("pfmanager.proyek"):obj>/assessment/',
        auth='public',
        methods=['GET'])
    def daftar_assessment(self, obj, **kw):
        return http.request.render('pfmanager.listing', {
            'root': '/pfmanager',
            'objects': obj.assessment_id
        })

    @http.route(
        '/proyek/<model("pfmanager.proyek"):obj>/assessment/',
        auth='public',
        csrf=False,
        methods=['POST'])
    def tambah_assessment(self, obj, **kw):
        data, err = middleware_check_attrs(
            kw, ['kebutuhan', 'nama_narasumber', 'no_handphone']
        )
        if err:
            return data
        data['proyek_id'] = obj.id
        http.request.env['pfmanager.assessment'].sudo().create(data)
        return http.Response("Successfully created", status=201)

    @http.route(
        '/proyek/<model("pfmanager.proyek"):obj>/kebencanaan/',
        auth='public',
        methods=['GET'])
    def daftar_kebencanaan(self, obj, **kw):
        return http.request.render('pfmanager.listing', {
            'root': '/pfmanager',
            'objects': obj.kebencanaan_id
        })

    @http.route(
        '/proyek/<model("pfmanager.proyek"):obj>/kebencanaan/',
        auth='public',
        csrf=False,
        methods=['POST'])
    def tambah_kebencanaan(self, obj, **kw):
        data, err = middleware_check_attrs(
            kw, ['rincian_kebencanaan', 'lokasi', 'waktu_observasi']
        )
        if err:
            return data
        data['proyek_id'] = obj.id
        http.request.env['pfmanager.kebencanaan'].sudo().create(data)
        return http.Response("Successfully created", status=201)

    @http.route(
        '/proyek/<model("pfmanager.proyek"):obj>/peserta/',
        auth='public',
        methods=['GET'])
    def daftar_peserta(self, obj, **kw):
        return http.request.render('pfmanager.listing', {
            'root': '/pfmanager',
            'objects': obj.peserta_id
        })

    @http.route(
        '/proyek/<model("pfmanager.proyek"):obj>/peserta/',
        auth='public',
        csrf=False,
        methods=['POST'])
    def tambah_peserta(self, obj, **kw):
        data, err = middleware_check_attrs(
            kw, ['nama', 'tempat_tinggal', 'umur', 'email', 'no_handphone']
        )
        if err:
            return data
        data['proyek_id'] = obj.id
        http.request.env['pfmanager.peserta'].sudo().create(data)
        return "Successfully created"

    @http.route(
        '/proyek/<model("pfmanager.proyek"):obj>/kegiatan/',
        auth='public',
        methods=['GET'])
    def daftar_kegiatan(self, obj, **kw):
        return http.request.render('pfmanager.listing', {
            'root': '/pfmanager',
            'objects': obj.kegiatan_id
        })

    @http.route(
        '/proyek/<model("pfmanager.proyek"):obj>/kegiatan/',
        auth='public',
        csrf=False,
        methods=['POST'])
    def tambah_kegiatan(self, obj, **kw):
        data, err = middleware_check_attrs(
            kw, ['nama', 'waktu_mulai', 'waktu_akhir']
        )
        if err:
            return data
        data['proyek_id'] = obj.id
        http.request.env['pfmanager.kegiatan'].sudo().create(data)
        return http.Response("Successfully created", status=201)

class KegiatanController(http.Controller):
    @http.route(
        '/kegiatan/<model("pfmanager.kegiatan"):obj>/resource/',
        auth='public',
        methods=['GET'])
    def daftar_resource(self, obj, **kw):
        return http.request.render('pfmanager.listing', {
            'root': '/pfmanager',
            'objects': obj.resource_id
        })

    @http.route(
        '/kegiatan/<model("pfmanager.kegiatan"):obj>/resource/',
        auth='public',
        csrf=False,
        methods=['POST'])
    def tambah_resource(self, obj, **kw):
        data, err = middleware_check_attrs(
            kw, ['nama', 'waktu_mulai', 'waktu_akhir']
        )
        if err:
            return data
        data['proyek_id'] = obj.id
        http.request.env['pfmanager.resource'].sudo().create(data)
        return http.Response("Successfully created", status=201)


class PesertaController(http.Controller):
    @http.route(
        '/peserta/<model("pfmanager.peserta"):obj>/evaluasi/',
        auth='public',
        methods=['GET'])
    def daftar_evaluasi(self, obj, **kw):
        return http.request.render('pfmanager.listing', {
            'root': '/pfmanager',
            'objects': obj.evaluasi_id
        })

    @http.route(
        '/peserta/<model("pfmanager.peserta"):obj>/evaluasi/',
        auth='public',
        csrf=False,
        methods=['POST'])
    def tambah_evaluasi(self, obj, **kw):
        data, err = middleware_check_attrs(
            kw, ['evaluasi', 'nilai_performansi']
        )
        if err:
            return data
        data['peserta_id'] = obj.id
        http.request.env['pfmanager.evaluasi'].sudo().create(data)
        return http.Response("Successfully created", status=201)

    @http.route(
        '/evaluasi/<model("pfmanager.evaluasi"):obj>/',
        auth='public',
        csrf=False,
        methods=['PUT'])
    def edit_evaluasi(self, obj, **kw):
        # Secure plz
        obj.write(kw)
        return "Successfully updated"

    @http.route(
        '/peserta/<model("pfmanager.peserta"):obj>/progress/',
        auth='public',
        methods=['GET'])
    def daftar_progress(self, obj, **kw):
        return http.request.render('pfmanager.listing', {
            'root': '/pfmanager',
            'objects': obj.progress_id
        })

    @http.route(
        '/peserta/<model("pfmanager.peserta"):obj>/progress/',
        auth='public',
        csrf=False,
        methods=['POST'])
    def tambah_progress(self, obj, **kw):
        data, err = middleware_check_attrs(
            kw, ['bulan_ke', 'catatan']
        )
        if err:
            return data
        data['peserta_id'] = obj.id
        http.request.env['pfmanager.progress'].sudo().create(data)
        return http.Response("Successfully created", status=201)
