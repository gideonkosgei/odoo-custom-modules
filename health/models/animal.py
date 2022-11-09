# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthAnimal(models.Model):
    _name = "health.animal"
    _description = "Animal"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "animal_identification_number"

    client_id = fields.Many2one(comodel_name='health.client', string='Client', required=True,
                                tracking=True)
    animal_identification_number = fields.Char('Identification Number', required=True, tracking=True)
    breed_id = fields.Many2one(comodel_name='health.config.catalogue.item', string='Breed', required=True,
                               tracking=True)
    animal_age = fields.Float('Age', required=True, tracking=True)
    animal_type_id = fields.Many2one(comodel_name='health.config.catalogue.item', string='Animal Type', required=True,
                                     tracking=True)
    age_at_first_heat = fields.Integer('Age at first heat', required=True, tracking=True)
    interval_btw_2_3_successive_heats = fields.Integer('Interval between two/three successive heats, if not conceived',
                                                       required=True, tracking=True)
    age_at_first_calving = fields.Integer('Age at first calving', required=True, tracking=True)
    number_of_lactation = fields.Integer('No. of lactation', required=True, tracking=True)
    time_interval_btw_last_calving_to_next_heat = fields.Integer('Time interval between last calving to next heat',
                                                                 required=True, tracking=True)
    time_interval_btw_last_calving_to_next_conception = fields.Integer(
        'Time interval between last calving to next conception', required=True, tracking=True)
    type_of_mating = fields.Many2one(comodel_name='health.config.catalogue.item', string='Type Of Mating',
                                     required=True, tracking=True)
    date_of_service = fields.Date('Date of artificial insemination /natural mating', required=True, tracking=True)
    months_of_gestation_at_present = fields.Integer('Months of gestation at present, if conceived', required=True,
                                                    tracking=True)
    number_of_ai_per_conception = fields.Integer('No. of AI required per conception', required=True, tracking=True)

    general_appearance = fields.Many2one(comodel_name='health.config.catalogue.item', string='General Appearance',
                                         required=True, tracking=True)

    body_coat = fields.Many2one(comodel_name='health.config.catalogue.item', string='Body coat',
                                required=True, tracking=True)

    general_health_condition = fields.Many2one(comodel_name='health.config.catalogue.item',
                                               string='General health condition',
                                               required=True, tracking=True)

    appetite = fields.Many2one(comodel_name='health.config.catalogue.item', string='Appetite',
                               required=True, tracking=True)

    eyes = fields.Many2one(comodel_name='health.config.catalogue.item', string='Eyes',
                           required=True, tracking=True)

    number_location_of_wounds = fields.Integer('Number and location of any wounds >2 cm diameter', required=True,
                                               tracking=True)

    number_location_of_hair_loss_patches = fields.Integer('Number and location of any patches of hair loss >2 cm',
                                                          required=True, tracking=True)

    lameness = fields.Many2one(comodel_name='health.config.catalogue.item', string='Lameness',
                               required=True, tracking=True)

    body_temperature = fields.Float('Body Temperature(°C)', required=True, tracking=True)
    presence_of_injury_in_the_abdomen = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                        string='Presence of injury in the abdomen',
                                                        required=True, tracking=True)
    presence_of_external_parasite = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                    string='Presence of external parasite',
                                                    required=True, tracking=True)
    appearance_of_udder = fields.Many2one(comodel_name='health.config.catalogue.item',
                                          string='Appearance of udder',
                                          required=True, tracking=True)
    presence_of_injury_on_udder = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                  string='Presence of injury on udder',
                                                  required=True, tracking=True)
    hanging_out_of_placenta = fields.Many2one(comodel_name='health.config.catalogue.item',
                                              string='Hanging out of placenta',
                                              required=True, tracking=True)

    position_of_foetus = fields.Many2one(comodel_name='health.config.catalogue.item',
                                         string='Position of Foetus',
                                         required=True, tracking=True)

    water_bag = fields.Many2one(comodel_name='health.config.catalogue.item',
                                string='Water bag',
                                required=True, tracking=True)

    genital_discharge = fields.Many2one(comodel_name='health.config.catalogue.item',
                                        string='Genital discharge',
                                        required=True, tracking=True)

    colour_of_visible_mucous_membrane = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                        string='Colour of visible mucous membrane',
                                                        required=True, tracking=True)

    ease_of_handling = fields.Many2one(comodel_name='health.config.catalogue.item',
                                       string='Ease of handling (Stepping or kicking on examination)',
                                       required=True, tracking=True)

    delayed_post_partum_heat = fields.Many2one(comodel_name='health.config.catalogue.item',
                                               string='Delayed post-partum heat ', required=True, tracking=True)

    delayed_post_partum_heat_length = fields.Integer('Delay Length', required=True, tracking=True)

    repeat_breeding = fields.Many2one(comodel_name='health.config.catalogue.item', string='Repeat breeding',
                                      required=True, tracking=True)
    repeat_breeding_count = fields.Integer('Repeat Count', required=True, tracking=True)

    dystocia = fields.Many2one(comodel_name='health.config.catalogue.item', string='Dystocia', required=True,
                               tracking=True)

    dystocia_foetus_status = fields.Many2one(comodel_name='health.config.catalogue.item', string='Foetus Status',
                                             required=True,
                                             tracking=True)

    retention_of_placenta = fields.Many2one(comodel_name='health.config.catalogue.item',
                                            string='Retention of placenta', required=True, tracking=True)

    retention_of_placenta_count = fields.Integer('Retention Count', required=True, tracking=True)

    abortion = fields.Many2one(comodel_name='health.config.catalogue.item',
                               string='Abortion', required=True, tracking=True)

    still_birth = fields.Many2one(comodel_name='health.config.catalogue.item', string='Still birth', required=True,
                                  tracking=True)
    still_birth_count = fields.Integer('Still birth Count', required=True, tracking=True)

    mastitis = fields.Many2one(comodel_name='health.config.catalogue.item', string='Mastitis', required=True,
                               tracking=True)
    mastitis_quarters_affected = fields.Integer('Quarters Affected', required=True, tracking=True)

    teat_canal_blockage = fields.Many2one(comodel_name='health.config.catalogue.item',
                                          string='Is there any blockage of teat canal?', required=True, tracking=True)

    udder_fibrotic_change = fields.Many2one(comodel_name='health.config.catalogue.item',
                                            string='Is there any fibrotic change in the udder?', required=True,
                                            tracking=True)
    udder_fibrotic_change_status = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                   string='Fibrotic Change Status', tracking=True)

    hip_dislocation_fracture_history = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                       string='History of hip dislocation/fracture', required=True,
                                                       tracking=True)

    duration_of_the_existing_disease = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                       string='Duration of the existing disease', required=True,
                                                       tracking=True)

    lameness_history = fields.Many2one(comodel_name='health.config.catalogue.item', string='History of lameness',
                                       required=True, tracking=True)

    per_rectum_examination_findings = fields.Text('Findings of per rectum examination', required=True, tracking=True)
    rapid_tests_done = fields.Many2one(comodel_name='health.config.catalogue.item', string='Rapid Tests Done?',
                                       required=True, tracking=True)

    lab_test_recommended = fields.Text('Lab test recommended', required=True, tracking=True)
    lab_test_results = fields.Text('Lab test results', required=True, tracking=True)
    treatment_advice_given = fields.Text('Treatment / Advice given', required=True, tracking=True)

    vaccination_disease = fields.Text('Disease Vaccinated', required=True, tracking=True)
    vaccination_date = fields.Date('Vaccination Date', required=True, tracking=True)
    deworming_date = fields.Date('Deworming Date', required=True, tracking=True)
    nutritional_plan = fields.Many2one(comodel_name='health.config.catalogue.item', string='Nutritional Plan',
                                       required=True, tracking=True)

    regular_supply_of_minerals_and_vitamins = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                              string='Regular Supply Of Minerals & Vitamins',
                                                              required=True, tracking=True)
