# -*- coding: utf-8 -*-

from odoo import models, fields, api


class music_song(models.Model):
    _name = "music.song"

    name = fields.Char(String="Titel", required=True)
    erscheinungsdatum = fields.Date(String="Erscheinungsdatum")
    dauer = fields.Float(String="Dauer")
    album_id = fields.Many2one(comodel_name="music.album", String="Album")
    interpret_id = fields.Many2one(comodel_name="music.interpret", String="Interpret")
    genre_ids = fields.Many2many(comodel_name="music.genre", String="Genre")


class music_album(models.Model):
    _name = "music.album"

    name = fields.Char(String="Album", required=True)
    label = fields.Char(String="Label")
    anzahl_songs = fields.Integer(String="Anzahl Songs",
                                  compute="_compute_anzahl_songs")
    song_ids = fields.One2many(comodel_name="music.song",
                               inverse_name="album_id", String="Songs")
    interpret_id = fields.Many2one(comodel_name="music.interpret", String="Interpret")

    @api.depends("song_ids")
    def _compute_anzahl_songs(self):
        self.anzahl_songs = len(self.song_ids)


class music_interpret(models.Model):
    _name = "music.interpret"

    name = fields.Char(String="Name", required=True)
    album_ids = fields.One2many(comodel_name="music.album",
                                inverse_name="interpret_id", String="Alben")
    song_ids = fields.One2many(comodel_name="music.song",
                               inverse_name="interpret_id", String="Songs")


class music_genre(models.Model):
    _name = "music.genre"

    name = fields.Char(String="Name", required=True)
    song_ids = fields.Many2many(comodel_name="music.song", String="Songs")


# class music(models.Model):
#     _name = 'music.music'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100