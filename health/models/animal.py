# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthAnimal(models.Model):
    _name = "health.animal"
    _description = "Animal"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "animal_identification_number"

    farmer_id = fields.Many2one(comodel_name='health.farmer', string='Farmer', required=True,
                                tracking=True)
    animal_identification_number = fields.Char('Identification Number', tracking=True, required=True, )
    species_id = fields.Many2one(comodel_name='health.config.catalogue.item', string='Species',
                                 tracking=True, required=True)
    breed_id = fields.Many2one(comodel_name='health.breed', string='Breed',
                               tracking=True, required=True, domain="[('species_id', '=', species_id)]")
    animal_age = fields.Float('Age', tracking=True, required=True)
    animal_type_id = fields.Many2one(comodel_name='health.config.catalogue.item', string='Animal Type',
                                     tracking=True, required=True)
    age_at_first_heat = fields.Integer('Age at first heat(Months)', tracking=True)
    show_sign_of_heat_after_first_heat = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                         string='Show Sign Of Heat After First Heat',
                                                         tracking=True)
    interval_btw_2_3_successive_heats = fields.Integer('Interval Between Successive Heats (Days)',
                                                       tracking=True)
    age_at_first_calving = fields.Integer('Age at first calving(months)', tracking=True)
    number_of_lactation = fields.Integer('No. of lactation', tracking=True)
    time_interval_btw_last_calving_to_next_heat = fields.Integer(
        'Time interval between last calving to next heat(months)',
        tracking=True)
    time_interval_btw_last_calving_to_next_conception = fields.Integer(
        'Time interval between last calving to next conception(months)', tracking=True)
    type_of_mating = fields.Many2one(comodel_name='health.config.catalogue.item', string='Type Of Mating',
                                     tracking=True)
    date_of_service = fields.Date('Date of artificial insemination /natural mating', tracking=True)
    months_of_gestation_at_present = fields.Integer('Months of gestation at present, if conceived',
                                                    tracking=True)
    number_of_ai_per_conception = fields.Integer('No. of AI required per conception', tracking=True)

    general_appearance = fields.Many2one(comodel_name='health.config.catalogue.item', string='General Appearance',
                                         tracking=True)

    body_coat = fields.Many2one(comodel_name='health.config.catalogue.item', string='Body coat',
                                tracking=True)

    general_health_condition = fields.Many2one(comodel_name='health.config.catalogue.item',
                                               string='General health condition',
                                               tracking=True)

    appetite = fields.Many2one(comodel_name='health.config.catalogue.item', string='Appetite',
                               tracking=True)

    eyes = fields.Many2one(comodel_name='health.config.catalogue.item', string='Eyes',
                           tracking=True)

    number_location_of_wounds = fields.Integer('Number and location of any wounds >2 cm diameter',
                                               tracking=True)

    number_location_of_hair_loss_patches = fields.Integer('Number and location of any patches of hair loss >2 cm',
                                                          tracking=True)

    lameness = fields.Many2one(comodel_name='health.config.catalogue.item', string='Lameness',
                               tracking=True)

    body_temperature = fields.Float('Body Temperature(°C)', tracking=True)
    presence_of_injury_in_the_abdomen = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                        string='Presence of injury in the abdomen',
                                                        tracking=True)
    presence_of_external_parasite = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                    string='Presence of external parasite',
                                                    tracking=True)
    appearance_of_udder = fields.Many2one(comodel_name='health.config.catalogue.item',
                                          string='Appearance of udder',
                                          tracking=True)
    presence_of_injury_on_udder = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                  string='Presence of injury on udder',
                                                  tracking=True)
    hanging_out_of_placenta = fields.Many2one(comodel_name='health.config.catalogue.item',
                                              string='Hanging out of placenta',
                                              tracking=True)

    position_of_foetus = fields.Many2one(comodel_name='health.config.catalogue.item',
                                         string='Position of Foetus',
                                         tracking=True)

    water_bag = fields.Many2one(comodel_name='health.config.catalogue.item',
                                string='Water bag',
                                tracking=True)

    genital_discharge = fields.Many2one(comodel_name='health.config.catalogue.item',
                                        string='Genital discharge',
                                        tracking=True)

    colour_of_visible_mucous_membrane = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                        string='Colour of visible mucous membrane',
                                                        tracking=True)

    ease_of_handling = fields.Many2one(comodel_name='health.config.catalogue.item',
                                       string='Ease of handling (Stepping or kicking on examination)',
                                       tracking=True)

    delayed_post_partum_heat = fields.Many2one(comodel_name='health.config.catalogue.item',
                                               string='Delayed post-partum heat ', tracking=True)

    delayed_post_partum_heat_length = fields.Integer('Delay Length', tracking=True)

    repeat_breeding = fields.Many2one(comodel_name='health.config.catalogue.item', string='Repeat breeding',
                                      tracking=True)
    repeat_breeding_count = fields.Integer('Repeat Count', tracking=True)

    dystocia = fields.Many2one(comodel_name='health.config.catalogue.item', string='Dystocia',
                               tracking=True)

    dystocia_foetus_status = fields.Many2one(comodel_name='health.config.catalogue.item', string='Foetus Status',

                                             tracking=True)

    retention_of_placenta = fields.Many2one(comodel_name='health.config.catalogue.item',
                                            string='Retention of placenta', tracking=True)

    retention_of_placenta_count = fields.Integer('Retention Count', tracking=True)

    abortion = fields.Many2one(comodel_name='health.config.catalogue.item',
                               string='Abortion', tracking=True)

    still_birth = fields.Many2one(comodel_name='health.config.catalogue.item', string='Still birth',
                                  tracking=True)
    still_birth_count = fields.Integer('Still birth Count', tracking=True)

    mastitis = fields.Many2one(comodel_name='health.config.catalogue.item', string='Mastitis',
                               tracking=True)
    mastitis_quarters_affected = fields.Integer('Quarters Affected', tracking=True)

    teat_canal_blockage = fields.Many2one(comodel_name='health.config.catalogue.item',
                                          string='Is there any blockage of teat canal?', tracking=True)

    udder_fibrotic_change = fields.Many2one(comodel_name='health.config.catalogue.item',
                                            string='Is there any fibrotic change in the udder?',
                                            tracking=True)
    udder_fibrotic_change_status = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                   string='Fibrotic Change Status', tracking=True)

    hip_dislocation_fracture_history = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                       string='History of hip dislocation/fracture',
                                                       tracking=True)

    duration_of_the_existing_disease = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                       string='Duration of the existing disease',
                                                       tracking=True)

    lameness_history = fields.Many2one(comodel_name='health.config.catalogue.item', string='History of lameness',
                                       tracking=True)

    per_rectum_examination_findings = fields.Text('Findings of per rectum examination', tracking=True)
    rapid_tests_done = fields.Many2one(comodel_name='health.config.catalogue.item', string='Rapid Tests Done?',
                                       tracking=True)

    lab_test_recommended = fields.Text('Lab test recommended', tracking=True)
    lab_test_results = fields.Text('Lab test results', tracking=True)
    treatment_advice_given = fields.Text('Treatment / Advice given', tracking=True)

    vaccination_disease = fields.Text('Disease Vaccinated', tracking=True)
    vaccination_date = fields.Date('Vaccination Date', tracking=True)
    deworming_date = fields.Date('Deworming Date', tracking=True)
    nutritional_plan = fields.Many2one(comodel_name='health.config.catalogue.item', string='Nutritional Plan',
                                       tracking=True)

    regular_supply_of_minerals_and_vitamins = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                              string='Regular Supply Of Minerals & Vitamins',
                                                              tracking=True)
