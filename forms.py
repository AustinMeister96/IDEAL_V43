from django import forms
from django.forms import ModelForm, RadioSelect
from .models import Blood_Collection, Breath_Collection, Indirect_costs, Stai_y1_2, Veterans_rand_12, ct_scan_baseline, ct_scan_t1, ct_scan_t2, ct_scan_t3, ct_scan_t4, ct_scan_t5, ct_scan_t6, ct_scan_t7,  Exposure, Exposure2, Exposure3, Mandatory_questionaire, Mandatory_questionaire_c, Mandatory_questionaire_de, Mandatory_questionaire_fg, inclusion, Participant, ct_scan_nodule_1,ct_scan_nodule_2, ct_scan_nodule_3, ct_scan_nodule_4, ct_scan_nodule_5 ,biological_relatives_with_cancer, annual_study_update_part_a, annual_study_update_medications, annual_study_update_part_b, annual_study_update, last_mandatory_questionnaire, Protocol_Deviations, Clinical_Procedures, lab_processing
from django.utils.safestring import mark_safe
from .models import PLCO_score
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import formset_factory


class Blood_Collection_Form(forms.ModelForm):
    class Meta:
        model = Blood_Collection
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateTimeInput(attrs={'type': 'date', 'max':'9999-12-31'}),
            'date_of_collection': forms.DateTimeInput(attrs={'type': 'date', 'max':'9999-12-31'}),
            'time_collected': forms.TimeInput(attrs={'type': 'time', 'max':'9999-12-31'}),
            'processing_start_time': forms.TimeInput(attrs={'type': 'time', 'max':'9999-12-31'}),
            'time_placed_freezer': forms.TimeInput(attrs={'type': 'time', 'max':'9999-12-31'}),
            'collected_by': forms.TextInput(attrs={}),
            'visit_type': forms.TextInput(attrs={}),
            'comments': forms.TextInput(attrs={}),
            'ideal_participant_num': forms.NumberInput(attrs={'class': ''}),
            'freezer_box_num': forms.NumberInput(attrs={'class': ''}),
            'y_plasma_barcode_1': forms.NumberInput(attrs={'class': ''}),
            'y_plasma_barcode_2': forms.NumberInput(attrs={'class': ''}),
            'p_plasma_barcode_1': forms.NumberInput(attrs={'class': ''}),
            'p_plasma_barcode_2': forms.NumberInput(attrs={'class': ''}),
            'r_rbc_barcode_1': forms.NumberInput(attrs={'class': ''}),
            'r_rbc_barcode_2': forms.NumberInput(attrs={'class': ''}),
            'y_bottom_barcode_1': forms.NumberInput(attrs={'class': ''}),
            'y_bottom_barcode_2': forms.NumberInput(attrs={'class': ''}),
            'p_bottom_barcode_1': forms.NumberInput(attrs={'class': ''}),
            'p_bottom_barcode_2': forms.NumberInput(attrs={'class': ''}),

            'y_plasma_volume_1': forms.Select(attrs={'class': ''}),
            'y_plasma_volume_2': forms.Select(attrs={'class': ''}),
            'y_plasma_bottom_volume_1': forms.Select(attrs={'class': ''}),
            'y_plasma_bottom_volume_2': forms.Select(attrs={'class': ''}),
            'p_plasma_volume_1': forms.Select(attrs={'class': ''}),
            'p_plasma_volume_2': forms.Select(attrs={'class': ''}),
            'p_plasma_bottom_volume_1': forms.Select(attrs={'class': ''}),
            'p_plasma_bottom_volume_2': forms.Select(attrs={'class': ''}),
            'r_rbc_volume_1': forms.Select(attrs={'class': ''}),
            'r_rbc_volume_2': forms.Select(attrs={'class': ''}),
            'r_rbc_bottom_volume_1': forms.Select(attrs={'class': ''}),
            'r_rbc_bottom_volume_2': forms.Select(attrs={'class': ''}),
        }

class DateInput(forms.DateInput):
    input_type = 'date'



class customTimeInput(forms.TimeInput):
    input_type = 'time'
    format = '%M:%S'

class customTimeWidget(forms.MultiWidget):
    widget = customTimeInput

class Breath_Collection_Form(forms.ModelForm):
    YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No')
    ]
    MASK_TYPE_CHOICES = [
        ('Mouthpiece', 'Mouthpiece'),
        ('Mask', 'Mask'),
    ]
    brush_teeth = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    mouthwash = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    face_cream = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    perfume_cologne = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    deodorant = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    smoke_exposure = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    fuel_car = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    short_of_breath = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    fever = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    cough = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    cold = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    no_symptoms = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    halitosis = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    aborted = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    incomplete = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    declined = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    pneumonia = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    inhaled_medication = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    hrt = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    grt = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    birth_control = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )

    class Meta:
        model = Breath_Collection
        fields = '__all__'
        widgets = {
            'collection_date': forms.DateInput(attrs={'type': 'date','class': '', 'max': '9999-12-31'}),
            'collection_time': forms.TimeInput(attrs={'type': 'time','class': ''}),
            'brush_teeth_time': forms.TimeInput(attrs={'type': 'time','class': ''}),
            'last_meal_hours_ago': forms.NumberInput(attrs={'class': ''}),
            'last_meal_minutes_ago': forms.NumberInput(attrs={'class': ''}),
            'last_drink_hours_ago': forms.NumberInput(attrs={'class': ''}),
            'last_drink_minutes_ago': forms.NumberInput(attrs={'class': ''}),
            'collection_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'collection_stop_time': forms.TimeInput(attrs={'type': 'time'}),
            'collected_by': forms.TextInput(attrs={'class': ''}),
            'location': forms.TextInput(attrs={'class': ''}),
            'arrival_type': forms.Select(attrs={'class': ''}),
            'last_meal': forms.TextInput(attrs={'class': ''}),
            'last_drink': forms.TextInput(attrs={'class': ''}),
            'notes': forms.Textarea(attrs={'class': '', 'style': 'height: 150px;'}),
            'reciva_barcode': forms.NumberInput(attrs={'class': ''}),
            'tennax_number': forms.NumberInput(attrs={'class': ''}),
            'casper_flow': forms.NumberInput(attrs={'class': ''}),
            'collection_duration_minutes': forms.NumberInput(attrs={'class': ''}),
            'collection_duration_seconds': forms.NumberInput(attrs={'class': ''}),
            'breathing_rate': forms.NumberInput(attrs={'class': ''}),
            'room_air_barcode': forms.NumberInput(attrs={'class': ''}),
            'room_air_tennax': forms.NumberInput(attrs={'class': ''}),
            'casper_barcode': forms.NumberInput(attrs={'class': ''}),
            'casper_tennax': forms.NumberInput(attrs={'class': ''}),
            'reciva_tennax': forms.NumberInput(attrs={'class': ''}),
            'reciva_flow': forms.NumberInput(attrs={'class': ''}),
            'reciva_duration': forms.NumberInput(attrs={'class': ''}),
            'reciva_breathing_rate': forms.NumberInput(attrs={'class': ''}),
            'brush_teeth': forms.CheckboxInput(attrs={'class': ''}),
            'smoke_exposure': forms.CheckboxInput(attrs={'class': ''}),
            'fuel_car': forms.CheckboxInput(attrs={'class': ''}),
            'short_of_breath': forms.CheckboxInput(attrs={'class': ''}),
            'fever': forms.CheckboxInput(attrs={'class': ''}),
            'cough': forms.CheckboxInput(attrs={'class': ''}),
            'cold': forms.CheckboxInput(attrs={'class': ''}),
            'no_symptoms': forms.CheckboxInput(attrs={'class': ''}),
            'halitosis': forms.CheckboxInput(attrs={'class': ''}),
            'aborted': forms.CheckboxInput(attrs={'class': ''}),
            'incomplete': forms.CheckboxInput(attrs={'class': ''}),
            'declined': forms.CheckboxInput(attrs={'class': ''}),
            'volume_collected': forms.NumberInput(attrs={'class': ''}),
            'birth_control': forms.CheckboxInput(attrs={'class': ''}),
            'birth_control_duration': forms.NumberInput(attrs={'class': ''}),
            'birth_control_duration_unit': forms.RadioSelect(attrs={'class': ''}),
            'menopausal': forms.RadioSelect(attrs={'class': ''}),
            'hrt': forms.RadioSelect(attrs={'class': ''}),
            'hrt_duration': forms.NumberInput(attrs={'class': ''}),
            'hrt_duration_unit': forms.RadioSelect(attrs={'class': ''}),
            'grt': forms.RadioSelect(attrs={'class': ''}),
            'grt_duration': forms.NumberInput(attrs={'class': ''}),
            'grt_duration_unit': forms.RadioSelect(attrs={'class': ''}),
            'gender_affirming_surgery': forms.CheckboxInput(attrs={'class': ''}),
            'gender_affirming_type': forms.TextInput(attrs={'class': ''}),
            'inhaled_medication': forms.CheckboxInput(attrs={'class': ''}),
            'inhaled_medication_type': forms.TextInput(attrs={'class': ''}),
            'inhaled_medication_brand': forms.TextInput(attrs={'class': ''}),
            'inhaled_medication_name': forms.TextInput(attrs={'class': ''}),
            'inhaled_medication_last_taken': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'pneumonia': forms.CheckboxInput(attrs={'class': ''}),
            'smoke_exposure_type': forms.TextInput(attrs={'class': ''}),
            'room_air_collection_time': forms.TimeInput(attrs={'type': 'time', 'class': ''}),
            'casper_collection_time': forms.TimeInput(attrs={'type': 'time', 'class': ''}),
            'reciva_mouthpiece_type': forms.RadioSelect(attrs={'class': ''}),   
        }

# class Lab_Processing_Form(forms.ModelForm):

#     #lab_processing_upload = forms.FileField()

#     class Meta:
#         model = lab_processing
#         fields = ['participant_num', 'lab_processing_upload'] 
#         # widgets = {
#         #     'lab_processing_upload': forms.FileInput(attrs={'class': 'btn-green'}),
#         # }

class Lab_Processing_Form(forms.ModelForm):
    def __init__(self, *args, participant_id=None, **kwargs):
        super(Lab_Processing_Form, self).__init__(*args, **kwargs)
        if participant_id:
            self.fields['participant_num'].initial = participant_id

    class Meta:
        model = lab_processing
        fields = ['participant_num', 'lab_processing_upload']

from .models import mandatory_questionaire_dashboard

class mandatory_questionaire_dashboard_form(forms.ModelForm):
    def __init__(self, *args, participant_id=None, **kwargs):
        super(mandatory_questionaire_dashboard_form, self).__init__(*args, **kwargs)
        if participant_id:
            self.fields['participant_num'].initial = participant_id

    class Meta:
        model = mandatory_questionaire_dashboard
        fields = ['participant_num', 'lab_processing_upload']

class BooleanRadioSelect(forms.RadioSelect):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        for i, (option_value, option_label) in enumerate(self.choices):
            radio_attrs = self.build_attrs(self.attrs.copy(), attrs)
            radio_attrs['type'] = 'radio'
            radio_attrs['name'] = name
            radio_attrs['value'] = forms.check_test(value, str(option_value))
            if option_value == value:
                radio_attrs['checked'] = True

            label_for = f' id="{attrs["id"]}_{i}"' if 'id' in attrs else ''
            label_attrs = self.build_attrs({'for': f'{attrs["id"]}_{i}'})

            option_label = forms.html.escape(option_label)
            radio = f'<input{self.flatatt(radio_attrs)} />'
            label = f'<label{self.flatatt(label_attrs)}>{option_label}</label>'
            output.append(f'<div>{radio} {label}</div>')

        return mark_safe('\n'.join(output))
    


class Exposure_Form(forms.Form):

    class Meta:
        model = Exposure2
        fields = '__all__'
        widgets = {
            'total_exposure': forms.Select(attrs={'class': ''}),
            'asbestos_exposure': forms.RadioSelect(attrs={'class': ''}),
            'asbestos_exposure_duration': forms.NumberInput(attrs={'class': ''}),
            'asbestos_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'silica_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'silica_exposure_duration': forms.NumberInput(attrs={'class': ''}),
            'silica_exposure': forms.RadioSelect(attrs={'class': ''}),
            'diesel': forms.RadioSelect(attrs={'class': ''}),
            'diesel_duration': forms.NumberInput(attrs={'class': ''}),
            'diesel_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'radon': forms.RadioSelect(attrs={'class': ''}),
            'radon_duration': forms.NumberInput(attrs={'class': ''}),
            'radon_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'cadmium': forms.RadioSelect(attrs={'class': ''}),
            'cadmium_duration': forms.NumberInput(attrs={'class': ''}),
            'cadmium_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'chromium': forms.RadioSelect(attrs={'class': ''}),
            'chromium_duration': forms.NumberInput(attrs={'class': ''}),
            'chromium_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'coal': forms.RadioSelect(attrs={'class': ''}),
            'coal_duration': forms.NumberInput(attrs={'class': ''}),
            'coal_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'arsenic': forms.RadioSelect(attrs={'class': ''}),
            'arsenic_duration': forms.NumberInput(attrs={'class': ''}),
            'arsenic_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'nickel': forms.NumberInput(attrs={'class': ''}),
            'nickel_duration': forms.NumberInput(attrs={'class': ''}),
            'nickel_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'plutonium': forms.RadioSelect(attrs={'class': ''}),
            'plutonium_duration': forms.NumberInput(attrs={'class': ''}),
            'plutonium_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'beryllium': forms.RadioSelect(attrs={'class': ''}),
            'beryllium_duration': forms.NumberInput(attrs={'class': ''}),
            'beryllium_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'ether': forms.RadioSelect(attrs={'class': ''}),
            'ether_duration': forms.NumberInput(attrs={'class': ''}),
            'ether_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'soot': forms.RadioSelect(attrs={'class': ''}),
            'soot_duration': forms.NumberInput(attrs={'class': ''}),
            'soot_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'welding': forms.RadioSelect(attrs={'class': ''}),
            'welding_duration': forms.NumberInput(attrs={'class': ''}),
            'welding_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'radiation': forms.RadioSelect(attrs={'class': ''}),
            'radiation_duration': forms.NumberInput(attrs={'class': ''}),
            'radiation_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'munitions': forms.RadioSelect(attrs={'class': ''}),
            'munitions_duration': forms.NumberInput(attrs={'class': ''}),
            'munitions_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'warfare': forms.RadioSelect(attrs={'class': ''}),
            'warfare_duration': forms.NumberInput(attrs={'class': ''}),
            'warfare_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'acheson': forms.RadioSelect(attrs={'class': ''}),
            'acheson_duration': forms.NumberInput(attrs={'class': ''}),
            'acheson_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'aluminum': forms.RadioSelect(attrs={'class': ''}),
            'aluminum_duration': forms.NumberInput(attrs={'class': ''}),
            'aluminum_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'coke': forms.RadioSelect(attrs={'class': ''}),
            'coke_duration': forms.NumberInput(attrs={'class': ''}),
            'coke_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'mining': forms.RadioSelect(attrs={'class': ''}),
            'mining_duration': forms.NumberInput(attrs={'class': ''}),
            'mining_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'iron': forms.RadioSelect(attrs={'class': ''}),
            'iron_duration': forms.NumberInput(attrs={'class': ''}),
            'iron_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'sand': forms.RadioSelect(attrs={'class': ''}),
            'sand_duration': forms.NumberInput(attrs={'class': ''}),
            'sand_exposure_age': forms.NumberInput(attrs={'class': ''}),
            
        }


class Exposure_Form2(forms.ModelForm):
    YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No')
    ]

    kitchen_range = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    cooking = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    cooking_chimney = forms.BooleanField(required=False)
    cooking_exhaust_fan = forms.BooleanField(required=False)
    cooking_open_window = forms.BooleanField(required=False)
    cooking_partial_open = forms.BooleanField(required=False)
    class Meta:
        model = Exposure2
        fields = '__all__'
        widgets = {
            'total_exposure': forms.Select(attrs={'class': ' in-line'}),
            'asbestos_exposure': forms.RadioSelect(attrs={'class': ''}),
            'asbestos_exposure_duration': forms.NumberInput(attrs={'class': ''}),
            'asbestos_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'silica_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'silica_exposure_duration': forms.NumberInput(attrs={'class': ''}),
            'silica_exposure': forms.RadioSelect(attrs={'class': ''}),
            'diesel': forms.RadioSelect(attrs={'class': ''}),
            'diesel_duration': forms.NumberInput(attrs={'class': ''}),
            'diesel_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'radon': forms.RadioSelect(attrs={'class': ''}),
            'radon_duration': forms.NumberInput(attrs={'class': ''}),
            'radon_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'cadmium': forms.RadioSelect(attrs={'class': ''}),
            'cadmium_duration': forms.NumberInput(attrs={'class': ''}),
            'cadmium_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'chromium': forms.RadioSelect(attrs={'class': ''}),
            'chromium_duration': forms.NumberInput(attrs={'class': ''}),
            'chromium_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'coal': forms.RadioSelect(attrs={'class': ''}),
            'coal_duration': forms.NumberInput(attrs={'class': ''}),
            'coal_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'arsenic': forms.RadioSelect(attrs={'class': ''}),
            'arsenic_duration': forms.NumberInput(attrs={'class': ''}),
            'arsenic_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'nickel': forms.RadioSelect(attrs={'class': ''}),
            'nickel_duration': forms.NumberInput(attrs={'class': ''}),
            'nickel_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'plutonium': forms.RadioSelect(attrs={'class': ''}),
            'plutonium_duration': forms.NumberInput(attrs={'class': ''}),
            'plutonium_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'beryllium': forms.RadioSelect(attrs={'class': ''}),
            'beryllium_duration': forms.NumberInput(attrs={'class': ''}),
            'beryllium_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'ether': forms.RadioSelect(attrs={'class': ''}),
            'ether_duration': forms.NumberInput(attrs={'class': ''}),
            'ether_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'soot': forms.RadioSelect(attrs={'class': ''}),
            'soot_duration': forms.NumberInput(attrs={'class': ''}),
            'soot_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'welding': forms.RadioSelect(attrs={'class': ''}),
            'welding_duration': forms.NumberInput(attrs={'class': ''}),
            'welding_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'radiation': forms.RadioSelect(attrs={'class': ''}),
            'radiation_duration': forms.NumberInput(attrs={'class': ''}),
            'radiation_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'munitions': forms.RadioSelect(attrs={'class': ''}),
            'munitions_duration': forms.NumberInput(attrs={'class': ''}),
            'munitions_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'warfare': forms.RadioSelect(attrs={'class': ''}),
            'warfare_duration': forms.NumberInput(attrs={'class': ''}),
            'warfare_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'acheson': forms.RadioSelect(attrs={'class': ''}),
            'acheson_duration': forms.NumberInput(attrs={'class': ''}),
            'acheson_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'aluminum': forms.RadioSelect(attrs={'class': ''}),
            'aluminum_duration': forms.NumberInput(attrs={'class': ''}),
            'aluminum_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'coal_gasification': forms.RadioSelect(attrs={'class': ''}),
            'coal_gasification_duration': forms.NumberInput(attrs={'class': ''}),
            'coal_gasification_exposure_age': forms.NumberInput(attrs={'class': ''}),
            'coke': forms.RadioSelect(attrs={'class': ''}),
            'coke_duration': forms.TextInput(attrs={'class': ''}),
            'coke_exposure_age': forms.TextInput(attrs={'class': ''}),
            'sulfur': forms.RadioSelect(attrs={'class': ''}),
            'sulfur_duration': forms.TextInput(attrs={'class': ''}),
            'sulfur_exposure_age': forms.TextInput(attrs={'class': ''}),
            'mining': forms.RadioSelect(attrs={'class': ''}),
            'mining_duration': forms.TextInput(attrs={'class': ''}),
            'mining_exposure_age': forms.TextInput(attrs={'class': ''}),
            'iron': forms.RadioSelect(attrs={'class': ''}),
            'iron_duration': forms.TextInput(attrs={'class': ''}),
            'iron_exposure_age': forms.TextInput(attrs={'class': ''}),
            'painting': forms.RadioSelect(attrs={'class': ''}),
            'painting_duration': forms.TextInput(attrs={'class': ''}),
            'painting_exposure_age': forms.TextInput(attrs={'class': ''}),
            'rubber': forms.RadioSelect(attrs={'class': ''}),
            'rubber_duration': forms.TextInput(attrs={'class': ''}),
            'rubber_exposure_age': forms.TextInput(attrs={'class': ''}),
            'burn_pits': forms.RadioSelect(attrs={'class': ''}),
            'burn_pits_duration': forms.TextInput(attrs={'class': ''}),
            'burn_pits_exposure_age': forms.TextInput(attrs={'class': ''}),
            'oil_fires': forms.RadioSelect(attrs={'class': ''}),
            'oil_fires_duration':  forms.TextInput(attrs={'class': ''}),
            'oil_fires_exposure_age': forms.TextInput(attrs={'class': ''}),
            'sulfur_fires': forms.RadioSelect(attrs={'class': ''}),
            'sulfur_fires_duration': forms.TextInput(attrs={'class': ''}),
            'sulfur_fires_exposure_age': forms.TextInput(attrs={'class': ''}),
            'atsugi': forms.RadioSelect(attrs={'class': ''}),
            'atsugi_duration': forms.TextInput(attrs={'class': ''}),
            'atsugi_exposure_age': forms.TextInput(attrs={'class': ''}),
            'sand_storms': forms.RadioSelect(attrs={'class': ''}),
            'sand_storms_duration': forms.TextInput(attrs={'class': ''}),
            'sand_storms_exposure_age': forms.TextInput(attrs={'class': ''}),
            'job_held': forms.TextInput(attrs={'class': ''}),
            'job_held_duration': forms.TextInput(attrs={'class': ''}),
            'job_held_industry': forms.TextInput(attrs={'class': ''}),
            'job_held_2': forms.TextInput(attrs={'class': ''}),
            'job_held_2_duration': forms.TextInput(attrs={'class': ''}),
            'job_held_2_industry': forms.TextInput(attrs={'class': ''}),
            'job_held_3': forms.TextInput(attrs={'class': ''}),
            'job_held_3_duration': forms.TextInput(attrs={'class': ''}),
            'job_held_3_industry': forms.TextInput(attrs={'class': ''}),
            'duration_outdoor_pollution': forms.TextInput(attrs={'class': ''}),
            'duraiton_indoor_pollution': forms.TextInput(attrs={'class': ''}),
            'cooking_location': forms.RadioSelect(attrs={'style': 'display: inline;', 'style' : 'margin-right: 5px;'}),
            #'cooking_appliances': forms.CheckboxSelectMultiple(attrs={'class': ''}),
            'cooking_chimney': forms.CheckboxInput(attrs={'class': ''}),
            'cooking_exhaust_fan' : forms.CheckboxInput(attrs={'class': ''}),
            'cooking_open_window': forms.CheckboxInput(attrs={'class': ''}),
            'cooking_partial_open' : forms.CheckboxInput(attrs={'class': ''}),

            'cooking': forms.RadioSelect(attrs={'class': ''}),
            'frequency_in_cooking_location': forms.Select(attrs={'class': ''}),
            'kitchen_range': forms.BooleanField(required=False),
            'kitchen_range_age': forms.TextInput(attrs={'class': ''}),
            'cooking_0_20_frequency': forms.Select(attrs={'class': ''}),
            'cooking_0_20_frequency_times': forms.TextInput(attrs={'class': ''}),
            'cooking_0_20_fuel': forms.Select(attrs={'class': ''}),
            'cooking_0_20_fuel_other': forms.TextInput(attrs={'class': ''}),
            'cooking_0_20_cooking_oil': forms.Select(attrs={'class': ''}),
            'cooking_0_20_cooking_oil_store': forms.TextInput(attrs={'class': ''}),
            'cooking_0_20_cooking_oil_homemade': forms.TextInput(attrs={'class': ''}),
            'cooking_0_20_cooking_oil_other': forms.TextInput(attrs={'class': ''}),
            'cooking_0_20_saute_frequency': forms.TextInput(attrs={'class': ''}),
            'cooking_0_20_fry_frequency': forms.TextInput(attrs={'class': ''}),
            'cooking_0_20_deepfry_frequency': forms.TextInput(attrs={'class': ''}),
            'cooking_21_40_frequency': forms.Select(attrs={'class': ''}),
            'cooking_21_40_frequency_times': forms.TextInput(attrs={'class': ''}),
            'cooking_21_40_fuel': forms.Select(attrs={'class': ''}),
            'cooking_21_40_fuel_other': forms.TextInput(attrs={'class': ''}),
            'cooking_21_40_cooking_oil': forms.Select(attrs={'class': ''}),
            'cooking_21_40_cooking_oil_store': forms.TextInput(attrs={'class': ''}),
            'cooking_21_40_cooking_oil_homemade': forms.TextInput(attrs={'class': ''}),
            'cooking_21_40_cooking_oil_other': forms.TextInput(attrs={'class': ''}),
            'cooking_21_40_saute_frequency': forms.TextInput(attrs={'class': ''}),
            'cooking_21_40_fry_frequency': forms.TextInput(attrs={'class': ''}),
            'cooking_21_40_deepfry_frequency': forms.TextInput(attrs={'class': ''}),
            'cooking_41_60_frequency': forms.Select(attrs={'class': ''}),
            'cooking_41_60_frequency_times': forms.TextInput(attrs={'class': ''}),
            'cooking_41_60_fuel': forms.Select(attrs={'class': ''}),
            'cooking_41_60_fuel_other': forms.TextInput(attrs={'class': ''}),
            'cooking_41_60_cooking_oil': forms.Select(attrs={'class': ''}),
            'cooking_41_60_cooking_oil_store': forms.TextInput(attrs={'class': ''}),
            'cooking_41_60_cooking_oil_homemade': forms.TextInput(attrs={'class': ''}),
            'cooking_41_60_cooking_oil_other': forms.TextInput(attrs={'class': ''}),
            'cooking_41_60_saute_frequency': forms.TextInput(attrs={'class': ''}),
            'cooking_41_60_fry_frequency': forms.TextInput(attrs={'class': ''}),
            'cooking_41_60_deepfry_frequency': forms.TextInput(attrs={'class': ''}),
            'cooking_61_above_frequency': forms.Select(attrs={'class': ''}),
            'cooking_61_above_frequency_times': forms.TextInput(attrs={'class': ''}),
            'cooking_61_above_fuel': forms.Select(attrs={'class': ''}),
            'cooking_61_above_fuel_other': forms.TextInput(attrs={'class': ''}),
            'cooking_61_above_cooking_oil': forms.Select(attrs={'class': ''}),
            'cooking_61_above_cooking_oil_store': forms.TextInput(attrs={'class': ''}),
            'cooking_61_above_cooking_oil_homemade': forms.TextInput(attrs={'class': ''}),
            'cooking_61_above_cooking_oil_other': forms.TextInput(attrs={'class': ''}),
            'cooking_61_above_saute_frequency': forms.TextInput(attrs={'class': ''}),
            'cooking_61_above_fry_frequency': forms.TextInput(attrs={'class': ''}),
            'cooking_61_above_deepfry_frequency': forms.TextInput(attrs={'class': ''}),
            'processed_meat_frequency': forms.Select(attrs={'class': ''}),
            'red_meat_frequency': forms.Select(attrs={'class': ''}),


        }
    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        initial.setdefault('cooking_chimney', False)
        initial.setdefault('cooking_exhaust_fan', False)
        initial.setdefault('cooking_open_window', False)
        initial.setdefault('cooking_partial_open', False)
        kwargs['initial'] = initial
        super().__init__(*args, **kwargs)



class Exposure_Form3(ModelForm):
    class Meta:
        model = Exposure3
        fields = '__all__'
        widgets = {
            'home_1_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_1_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_1_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_1_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_1_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            # add the rest of the fields from the exposure3 model
            'home_2_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_province':forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_2_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_2_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_2_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_2_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_postal_code':forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_3_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_3_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_3_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_3_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_4_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_4_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_4_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_4_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_5_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_5_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_5_water_src_other':forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_5_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_6_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_6_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_6_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_6_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),

            'home_7_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_7_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_7_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_7_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_7_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_7_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_7_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_7_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_7_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_7_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_7_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_7_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_7_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_7_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_7_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_7_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_8_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_8_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_8_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_8_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_8_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_9_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_9_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_9_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_9_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_9_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_10_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_10_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_10_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_10_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_10_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_11_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_11_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_11_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_11_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_11_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_12_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_12_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_12_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_12_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_12_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_13_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_13_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_13_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_13_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_13_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_14_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_14_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_14_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_14_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_14_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_15_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_15_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_15_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_15_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_15_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_16_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_16_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_16_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_16_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_16_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_17_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_17_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_17_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_17_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_17_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_18_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_18_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_18_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_18_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_18_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_19_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_19_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_19_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_19_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_19_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_housing_type': forms.Select(attrs={'class': 'custom-class'}),
            'home_20_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_trucks': forms.Select(attrs={'class': 'custom-class'}),
            'home_20_water_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_20_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_20_heat_src': forms.Select(attrs={'class': 'custom-class'}),
            'home_20_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
        }



class Indirect_costs_form(forms.ModelForm):
    class Meta:
        model = Indirect_costs
        fields = '__all__'
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'procedure': forms.RadioSelect(attrs={'class': ''}),
            'procedure_other': forms.TextInput(attrs={'class': ''}),
            'missed_work': forms.RadioSelect(attrs={'class': ''}),
            'missed_work_hours': forms.NumberInput(attrs={'class': ''}),
            'affected_pay': forms.RadioSelect(attrs={'class': ''}),
            'appointment_time_hours': forms.NumberInput(attrs={'class': ''}),
            'appointment_time_minutes': forms.NumberInput(attrs={'class': ''}),
            'transportation': forms.RadioSelect(attrs={'class': ''}),
            'trip_distance': forms.NumberInput(attrs={'class': ''}),
            'parking_cost': forms.NumberInput(attrs={'class': ''}),
            'public_transportation_cost': forms.NumberInput(attrs={'class': ''}),
            'babysitter_cost': forms.NumberInput(attrs={'class': ''}),
            'other_cost': forms.NumberInput(attrs={'class': ''}),
            'other_costs_description': forms.TextInput(attrs={'class': ''}),
            'income': forms.Select(attrs={'class': ''}),
            'income_household': forms.Select(attrs={'class': ''}),
        }



class Stai_y1_2_form(forms.ModelForm):
    stai_y1_choices = [
        ('Not At All', 'Not At All'),
        ('Somewhat', 'Somewhat'),
        ('Moderately So', 'Moderately So'),
        ('Very Much So', 'Very Much So'),
    ]
    stai_y2_choices = [
        ('Almost Never', 'Almost Never'),
        ('Sometimes', 'Sometimes'),
        ('Often', 'Often'),
        ('Almost Always', 'Almost Always'),
    ]
    class Meta:
        model = Stai_y1_2
        fields = '__all__'
        widgets = {
            'entry_date': forms.DateInput(attrs={'type': 'date', 'class': '', 'max': '9999-12-31'}),
            'y1_feel_calm': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_secure': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_tense': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_strained': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_at_ease': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_upset': forms.RadioSelect(attrs={'class': ''}),
            'y1_worrying_misfortunes': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_satisfied': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_frightened': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_comfortable': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_self_confident': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_nervous': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_jittery': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_indecisive': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_relaxed': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_content': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_worried': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_confused': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_steady': forms.RadioSelect(attrs={'class': ''}),
            'y1_feel_pleasant': forms.RadioSelect(attrs={'class': ''}),
            'y2_feel_pleasant': forms.RadioSelect(attrs={'class': ''}),
            'y2_feel_nervous': forms.RadioSelect(attrs={'class': ''}),
            'y2_feel_satisfied': forms.RadioSelect(attrs={'class': ''}),
            'y2_wish_happy': forms.RadioSelect(attrs={'class': ''}),
            'y2_feel_failure': forms.RadioSelect(attrs={'class': ''}),
            'y2_feel_rested': forms.RadioSelect(attrs={'class': ''}),
            'y2_feel_calm': forms.RadioSelect(attrs={'class': ''}),
            'y2_difficulties_piling_up': forms.RadioSelect(attrs={'class': ''}),
            'y2_worry_doesnt_matter': forms.RadioSelect(attrs={'class': ''}),
            'y2_feel_happy': forms.RadioSelect(attrs={'class': ''}),
            'y2_disturbing_thoughts': forms.RadioSelect(attrs={'class': ''}),
            'y2_lack_confidence': forms.RadioSelect(attrs={'class': ''}),
            'y2_feel_secure': forms.RadioSelect(attrs={'class': ''}),
            'y2_decisions_easily': forms.RadioSelect(attrs={'class': ''}),
            'y2_feel_inadequate': forms.RadioSelect(attrs={'class': ''}),
            'y2_feel_content': forms.RadioSelect(attrs={'class': ''}),
            'y2_unimportant_thought_bother': forms.RadioSelect(attrs={'class': ''}),
            'y2_disappointments_keenly': forms.RadioSelect(attrs={'class': ''}),
            'y2_feel_steady': forms.RadioSelect(attrs={'class': ''}),
            'y2_state_of_tension': forms.RadioSelect(attrs={'class': ''}),
        }


class Veterans_rand_12_form(forms.ModelForm):
    general_health_choices = [
        ('Excellent', 'Excellent'),
        ('Very Good', 'Very Good'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor')
    ]
    limit_choices = [
        ('Yes, Limited a Lot', 'Yes, Limited a Lot'),
        ('Yes, Limited a Little', 'Yes, Limited a Little'),
        ('No, Not Limited at All', 'No, Not Limited at All')
    ]
    problems_choices = [
        ('No, None of the Time', 'No, None of the Time'),
        ('Yes, A Little of the Time', 'Yes, A Little of the Time'),
        ('Yes, Some of the Time', 'Yes, Some of the Time'),
        ('Yes, Most of the Time', 'Yes, Most of the Time'),
        ('Yes, All of the Time', 'Yes, All of the Time'),
    ]
    pain_interference_choices = [
        ('Not At All', 'Not At All'),
        ('A Little Bit', 'A Little Bit'),
        ('Moderately', 'Moderately'),
        ('Quite a Bit', 'Quite a Bit'),
        ('Extremely', 'Extremely')
    ]
    how_much_time_choices = [
        ('All of the Time', 'All of the Time'),
        ('Most of the Time', 'Most of the Time'),
        ('A Good Bit of the Time', 'A Good Bit of the Time'),
        ('Some of the Time', 'Some of the Time'),
        ('A Little of the Time', 'A Little of the Time'),
        ('None of the Time', 'None of the Time')
    ]
    social_interference_choices = [
        ('All of the Time', 'All of the Time'),
        ('Most of the Time', 'Most of the Time'),
        ('Some of the Time', 'Some of the Time'),
        ('A Little of the Time', 'A Little of the Time'),
        ('None of the Time', 'None of the Time')
    ]
    current_rating_choices = [
        ('Much Better', 'Much Better'),
        ('Slightly Better', 'Slightly Better'),
        ('About the Same', 'About the Same'),
        ('Slightly Worse', 'Slightly Worse'),
        ('Much Worse', 'Much Worse')
    ]
    class Meta:
        model = Veterans_rand_12
        fields = '__all__'
        widgets = {
            'rate_health': forms.RadioSelect(attrs={'class': ''}),
            'moderate_activities_limited': forms.RadioSelect(attrs={'class': ''}),
            'climbing_stairs_limited': forms.RadioSelect(attrs={'class': ''}),
            'physical_problems_accomplished_less': forms.RadioSelect(attrs={'class': ''}),
            'physical_problems_limited_work': forms.RadioSelect(attrs={'class': ''}),
            'emotional_problems_accomplished_less': forms.RadioSelect(attrs={'class': ''}),
            'emotional_problems_limited_work': forms.RadioSelect(attrs={'class': ''}),
            'pain_interfere_work': forms.RadioSelect(attrs={'class': ''}),
            'felt_calm': forms.RadioSelect(attrs={'class': ''}),
            'lot_of_energy': forms.RadioSelect(attrs={'class': ''}),
            'felt_downhearted': forms.RadioSelect(attrs={'class': ''}),
            'problems_interfere_social': forms.RadioSelect(attrs={'class': ''}),
            'compare_annual_physical_health': forms.RadioSelect(attrs={'class': ''}),
            'compare_annual_emotional_problems': forms.RadioSelect(attrs={'class': ''}),
        }



class Mandatory_questionaire_form(forms.ModelForm):
    YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No')
    ]
    copd = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    asthma = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    emphysema = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    chronic_bronchitis = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    hiv = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    long_covid = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    tuberculosis = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    adult_pneumonia = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    pulmonary_fibrosis = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    hypertension = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    diabetes = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    personal_cancer_history = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    initial=False
    )
    # YES_NO_DK_CHOICES = [
    # ('Yes', 'Yes'),
    # ('No', 'No'),
    # ('Don\'t Know', 'Don\'t Know')
    # ]
    # biological_relatives_cancer = forms.TypedChoiceField(
    # choices=YES_NO_DK_CHOICES,
    # widget=forms.RadioSelect(attrs={'class': 'radio'}),
    # coerce=lambda x: x == 'True'
    # )
    class Meta:
        model = Mandatory_questionaire
        fields = '__all__'
        widgets = {
            'initials': forms.TextInput(attrs={'class': ''}),
            'visit_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'current_height': forms.NumberInput(attrs={'class': ''}),
            'current_height_unit': forms.RadioSelect(attrs={'class': 'form-select-sm'}),
            'current_weight': forms.NumberInput(attrs={'class': ''}),
            'current_weight_unit': forms.RadioSelect(attrs={'class': 'form-select-sm'}),
            'sex_birth': forms.Select(attrs={'class': 'form-select-sm'}),
            'postal_code': forms.TextInput(attrs={'class': ''}),
            'current_age': forms.NumberInput(attrs={'class': ''}),
            'gender_identity': forms.Select(attrs={'class': 'form-select-sm'}),
            'gender_identity_other': forms.TextInput(attrs={'class': ''}),
            'gender_surgery_harmone': forms.Select(attrs={'class': 'form-select-sm'}),
            'ethinicity': forms.Select(attrs={'class': 'form-select-sm'}),
            'ethnicity_other': forms.TextInput(attrs={'class': ''}),
            'born_in_canada': forms.Select(attrs={'class': 'form-select-sm'}),
            'year_moved_to_canada': forms.TextInput(attrs={'class': ''}),
            'birthplace': forms.TextInput(attrs={'class': ''}),
            'highest_education_lvl': forms.Select(attrs={'class': 'form-select-sm'}),
            'highest_education_lvl_other': forms.TextInput(attrs={'class': ''}),
            'copd': forms.TextInput(attrs={'class': ''}),
            'emphysema': forms.TextInput(attrs={'class': ''}),
            'chronic_bronchitis': forms.TextInput(attrs={'class': ''}),
            'asthma': forms.TextInput(attrs={'class': ''}),
            'diabetes': forms.TextInput(attrs={'class': ''}),
            'hypertension': forms.TextInput(attrs={'class': ''}),
            'tuberculosis': forms.TextInput(attrs={'class': ''}),
            'adult_pneumonia': forms.TextInput(attrs={'class': ''}),
            'pulmonary_fibrosis': forms.TextInput(attrs={'class': ''}),
            'hiv': forms.TextInput(attrs={'class': ''}),
            'long_covid': forms.TextInput(attrs={'class': ''}),
            'personal_cancer_history': forms.TextInput(attrs={'class': ''}),
            'personal_cancer_history_youngest_age': forms.TextInput(attrs={'class': ''}),
            'personal_history_cancer_type': forms.TextInput(attrs={'class': ''}),
            'num_sisters': forms.TextInput(attrs={'class': ''}),
            'num_brothers': forms.TextInput(attrs={'class': ''}),
            'num_half_sisters': forms.TextInput(attrs={'class': ''}),
            'num_half_brothers': forms.TextInput(attrs={'class': ''}),
            'children': forms.TextInput(attrs={'class': ''}),
            # 'biological_relatives_cancer': forms.TextInput(attrs={'class': ''}),                      
        }



class biological_relatives_with_cancer_form(forms.ModelForm):
    class Meta:
        fields = '__all__'
        exclude = ['mandatory_questionaire', 'Id', 'participant_num']
        model = biological_relatives_with_cancer
        widgets = {
            'biological_relationship': forms.TextInput(attrs={'class': 'relatives'}),
            'type_of_cancer': forms.TextInput(attrs={'class': 'relatives'}),
            'diagnosis_age': forms.TextInput(attrs={'class': 'relatives'}),
        }



class MonthYearInput(forms.DateInput):
    input_type = 'month'

class Mandatory_questionaire_form_c(forms.ModelForm):
    YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No')
    ]
    
    smoked_more_100_cigs = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 

    )
    smoked_pipe = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    )
    stopped_smoking = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    )
    still_smoking_pipe = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    )
    still_smoke_cigars = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    )
    vape = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    )
    still_vape = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    )
    smoke_refrain = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    )
    smoke_morning = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    )
    smoke_sick = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    )
    quit_smoking = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    ) 
    marajuana_use = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    )      
    smoked_cigars = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False 
    )  

    class Meta:
        model = Mandatory_questionaire_c
        fields = '__all__'


        widgets = {
            'smoked_more_100_cigs': forms.TextInput(attrs={'class': ''}),
            'age_regular_smoking': forms.TextInput(attrs={'class': ''}),
            'avg_cig_per_day': forms.TextInput(attrs={'class': ''}),
            'stop_smoking': forms.TextInput(attrs={'class': ''}),
            'last_cig_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'last_cig_age': forms.TextInput(attrs={'class': ''}),
            'marajuana_use': forms.TextInput(attrs={'class': ''}),
            'marajuana_use_age_1': forms.TextInput(attrs={'class': ''}),
            'marajuana_use_to_age_1': forms.TextInput(attrs={'class': ''}),
            'marajuana_use_age_1_quantity': forms.Select(attrs={'class': ''}),
            'marajuana_use_age_1_mode': forms.Select(attrs={'class': ''}),
            'marajuana_use_age_1_units': forms.Select(attrs={'class': ''}),
            'marajuana_use_age_2': forms.TextInput(attrs={'class': ''}),
            'marajuana_use_to_age_2': forms.TextInput(attrs={'class': ''}),
            'marajuana_use_age_2_quantity': forms.Select(attrs={'class': ''}),
            'marajuana_use_age_2_mode': forms.Select(attrs={'class': ''}),
            'marajuana_use_age_2_units': forms.Select(attrs={'class': ''}),
            'marajuana_use_age_3': forms.TextInput(attrs={'class': ''}),
            'marajuana_use_to_age_3': forms.TextInput(attrs={'class': ''}),
            'marajuana_use_age_3_quantity': forms.Select(attrs={'class': ''}),
            'marajuana_use_age_3_mode': forms.Select(attrs={'class': ''}),
            'marajuana_use_age_3_units': forms.Select(attrs={'class': ''}),
            'marajuana_use_age_4': forms.TextInput(attrs={'class': ''}),
            'marajuana_use_to_age_4': forms.TextInput(attrs={'class': ''}),
            'marajuana_use_age_4_quantity': forms.Select(attrs={'class': ''}),
            'marajuana_use_age_4_mode': forms.Select(attrs={'class': ''}),
            'marajuana_use_age_4_units': forms.Select(attrs={'class': ''}),    
            'smoked_pipe': forms.TextInput(attrs={'class': ''}),
            'smoked_pipe_avg_ounces': forms.TextInput(attrs={'class': ''}),
            'smoked_pipe_avg_age': forms.TextInput(attrs={'class': ''}),
            'still_smoking_pipe': forms.TextInput(attrs={'class': ''}),
            'still_smoking_pipe_start_age': forms.TextInput(attrs={'class': ''}),
            'still_smoking_pipe_stop_age': forms.TextInput(attrs={'class': ''}),
            'smoked_cigars': forms.TextInput(attrs={'class': ''}),
            'avg_num_cigars': forms.TextInput(attrs={'class': ''}),
            'avg_cigar_age': forms.TextInput(attrs={'class': ''}),
            'still_smoke_cigars': forms.TextInput(attrs={'class': ''}),
            'still_smoke_cigars_start_age': forms.TextInput(attrs={'class': ''}),
            'chewing_tobacco': forms.Select(attrs={'class': ''}),
            'chewing_tobacco_age': forms.TextInput(attrs={'class': ''}),
            'chewing_tobacco_years': forms.TextInput(attrs={'class': ''}),
            'snuff': forms.Select(attrs={'class': ''}),
            'snuff_age': forms.TextInput(attrs={'class': ''}),
            'snuff_years': forms.TextInput(attrs={'class': ''}),
            'vape': forms.TextInput(attrs={'class': ''}),
            'vape_num_times': forms.TextInput(attrs={'class': ''}),
            'still_smoking_pipe_stop_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'still_smoking_pipe_start_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'still_smoke_cigars_stop_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'still_smoke_cigars_stop_age': forms.TextInput(attrs={'class': ''}),
            'still_smoke_cigars_start_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'vape_start_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'vape_stop_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'vape_start_age' : forms.TextInput(attrs={'class': ''}),
            'still_vape': forms.TextInput(attrs={'class': ''}),
            'still_vape_stop_age': forms.TextInput(attrs={'class': ''}),
            'still_vape_stop_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'vape_flavor': forms.TextInput(attrs={'class': ''}),
            'cigs_waking_up': forms.Select(attrs={'class': ''}),
            'smoke_refrain': forms.TextInput(attrs={'class': ''}),
            'cig_giveup': forms.Select(attrs={'class': ''}),
            'smoke_morning': forms.TextInput(attrs={'class': ''}),
            'smoke_sick': forms.TextInput(attrs={'class': ''}),
            'quit_smoking': forms.TextInput(attrs={'class': ''}),
            'quit_smoking_times': forms.TextInput(attrs={'class': ''}),
        }

    def __init__(self, *args, **kwargs):
        super(Mandatory_questionaire_form_c, self).__init__(*args, **kwargs)
        self.fields['quit_smoking_times'].required = False
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['quit_smoking_times'] = self.cleaned_data.get('quit_smoking_times', None)
        return cleaned_data

class Mandatory_questionaire_form_de(forms.ModelForm):
    YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No')
    ]
    second_hand_daily_choices = [
        ('Daily', 'Daily'),
        ('At Least 4 Days/Week but not everyday', 'At Least 4 Days/Week but not everyday'),
        ('1 - 3 Days/Week', '1 - 3 Days/Week'),
        ('Occasionally', 'Occasionally (less than 1 day/week)'),
    ]

    second_hand_1yr = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False
    )  
    alcohol = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False
    )   
    alcohol_current = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False
    )
    second_hand_daily = forms.TypedChoiceField(
    choices=second_hand_daily_choices,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    required=False
    )     
    class Meta:
        model = Mandatory_questionaire_de
        fields = '__all__'
        widgets = {
            'second_hand_smoke': forms.Select(attrs={'class': ''}),
            'second_hand_1yr': forms.RadioSelect(attrs={'class': ''}),
            'second_hand_home': forms.RadioSelect(attrs={'class': ''}),
            'second_hand_work': forms.RadioSelect(attrs={'class': ''}),
            'second_hand_leisure': forms.RadioSelect(attrs={'class': ''}),
            'second_hand_daily': forms.TextInput(attrs={'class': ''}),
            'second_hand_4days': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand_13days': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand_occasionally': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand_exposure_time': forms.RadioSelect(attrs={'class': ''}),
            'second_hand_yrs': forms.TextInput(attrs={'class': ''}),
            'second_hand_youth': forms.Select(attrs={'class': ''}),
            'second_hand_avg_exposure': forms.TextInput(attrs={'class': ''}),
            'alcohol': forms.RadioSelect(attrs={'class': ''}),
            'alcohol_from_age1': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_to_age1': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_beer1': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_wine1': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_liquor1': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_from_age2': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_to_age2': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_beer2': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_wine2': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_liquor2': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_from_age3': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_to_age3': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_beer3': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_wine3': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_liquor3': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_from_age4': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_to_age4': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_beer4': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_wine4': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_liquor4': forms.TextInput(attrs={'class': ' entry'}),
            'alcohol_current': forms.RadioSelect(attrs={'class': ' entry'}),
            'alcohol_stop_age': forms.TextInput(attrs={'class': ' entry'}),
        }
    
class Mandatory_questionaire_form_fg(forms.ModelForm):
    YES_NO_DK_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Don''t know', 'Don''t know')
    ]
    YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No')
    ]
    inhaled_drugs = forms.TypedChoiceField(
    choices=YES_NO_DK_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )   
    bronchodialators = forms.TypedChoiceField(
    choices=YES_NO_DK_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )   
    statins = forms.TypedChoiceField(
    choices=YES_NO_DK_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )  
    metformin = forms.TypedChoiceField(
    choices=YES_NO_DK_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    ) 
    occupation_exposure = forms.TypedChoiceField(
    choices=YES_NO_DK_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )      

    class Meta:
        model = Mandatory_questionaire_fg
        fields = '__all__'
        widgets = {
            'inhaled_drugs': forms.RadioSelect(attrs={'class': ''}),
            'inhaled_drugs_day': forms.TextInput(attrs={'class': ' entry'}),
            'inhaled_drugs_month': forms.TextInput(attrs={'class': ' entry'}),
            'inhaled_drugs_year': forms.TextInput(attrs={'class': ' entry'}),
            'inhaled_drugs_freq': forms.Select(attrs={'class': ''}),
            'bronchodialators': forms.RadioSelect(attrs={'class': ''}),
            'bronchodialators_day': forms.TextInput(attrs={'class': ' entry'}),
            'bronchodialators_month': forms.TextInput(attrs={'class': ' entry'}),
            'bronchodialators_year': forms.TextInput(attrs={'class': ' entry'}),
            'bronchodialators_freq': forms.Select(attrs={'class': ''}),
            'statins': forms.RadioSelect(attrs={'class': ''}),
            'statins_day': forms.TextInput(attrs={'class': ' entry'}),
            'statins_month': forms.TextInput(attrs={'class': ' entry'}),
            'statins_year': forms.TextInput(attrs={'class': ' entry'}),
            'statins_freq': forms.Select(attrs={'class': ''}),
            'metformin': forms.RadioSelect(attrs={'class': ''}),
            'metformin_day': forms.TextInput(attrs={'class': ' entry'}),
            'metformin_month': forms.TextInput(attrs={'class': ' entry'}),
            'metformin_year': forms.TextInput(attrs={'class': ' entry'}),
            'metformin_freq': forms.Select(attrs={'class': ''}),
            'current_working_situation': forms.Select(attrs={'class': ''}),
            'current_working_situation_other': forms.TextInput(attrs={'class': ''}),
            'occupation_longest': forms.TextInput(attrs={'class': ''}),
            'occupation_longest_activities': forms.TextInput(attrs={'class': ''}),
            'occupation_longest_years': forms.TextInput(attrs={'class': ''}),
            'occupation_exposure': forms.RadioSelect(attrs={'class': ''}),
            'occupation_fumes': forms.TextInput(attrs={'class': ''}),
            'occupation_years': forms.TextInput(attrs={'class': ''}),


            
        }


class last_mandatory_questionnaire_form(forms.ModelForm):
        YES_NO_DK_CHOICES = [
        (1, 'Yes'),
        (0, 'No'),
        (2, 'Don''t know')
        ]
        YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No')
        ]

        occupation_exposure = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        coerce=lambda x: x == 'True'
        )   
        second_hand_daily_choices = [
            ('Daily', 'Daily'),
            ('At Least 4 Days/Week but not everyday', 'At Least 4 Days/Week but not everyday'),
            ('1 - 3 Days/Week', '1 - 3 Days/Week'),
            ('Occasionally', 'Occasionally (less than 1 day/week)'),
        ]
 
        second_hand_1yr = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        coerce=lambda x: x == 'True',
        required=False
        )  
        alcohol = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        coerce=lambda x: x == 'True',
        required=False
        )   
        alcohol_current = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        coerce=lambda x: x == 'True',
        required=False
        )

        class Meta:
            model = last_mandatory_questionnaire
            fields = '__all__'
            widgets = {
                'inhaled_drugs': forms.RadioSelect(attrs={'class': ''}),
                'inhaled_drugs_day': forms.TextInput(attrs={'class': ' entry'}),
                'inhaled_drugs_month': forms.TextInput(attrs={'class': ' entry'}),
                'inhaled_drugs_year': forms.TextInput(attrs={'class': ' entry'}),
                'inhaled_drugs_freq': forms.Select(attrs={'class': ''}),
                'bronchodialators': forms.RadioSelect(attrs={'class': ''}),
                'bronchodialators_day': forms.TextInput(attrs={'class': ' entry'}),
                'bronchodialators_month': forms.TextInput(attrs={'class': ' entry'}),
                'bronchodialators_year': forms.TextInput(attrs={'class': ' entry'}),
                'bronchodialators_freq': forms.Select(attrs={'class': ''}),
                'statins': forms.RadioSelect(attrs={'class': ''}),
                'statins_day': forms.TextInput(attrs={'class': ' entry'}),
                'statins_month': forms.TextInput(attrs={'class': ' entry'}),
                'statins_year': forms.TextInput(attrs={'class': ' entry'}),
                'statins_freq': forms.Select(attrs={'class': ''}),
                'metformin': forms.RadioSelect(attrs={'class': ''}),
                'metformin_day': forms.TextInput(attrs={'class': ' entry'}),
                'metformin_month': forms.TextInput(attrs={'class': ' entry'}),
                'metformin_year': forms.TextInput(attrs={'class': ' entry'}),
                'metformin_freq': forms.Select(attrs={'class': ''}),
                'current_working_situation': forms.Select(attrs={'class': ''}),
                'current_working_situation_other': forms.TextInput(attrs={'class': ''}),
                'occupation_longest': forms.TextInput(attrs={'class': ''}),
                'occupation_longest_activities': forms.TextInput(attrs={'class': ''}),
                'occupation_longest_years': forms.TextInput(attrs={'class': ''}),
                'occupation_exposure': forms.RadioSelect(attrs={'class': ''}),
                'occupation_fumes': forms.TextInput(attrs={'class': ''}),
                'occupation_years': forms.TextInput(attrs={'class': ''}),
                'second_hand_smoke': forms.Select(attrs={'class': ''}),
                'second_hand_1yr': forms.RadioSelect(attrs={'class': ''}),
                'second_hand_home': forms.CheckboxInput(attrs={'class': 'checkbox-container in-line'}),
                'second_hand_work': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
                'second_hand_leisure': forms.CheckboxInput(attrs={}),
                'second_hand_daily': forms.RadioSelect(attrs={'class': ''}),
                'second_hand_4days': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
                'second_hand_13days': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
                'second_hand_occasionally': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
                'second_hand_exposure_time': forms.RadioSelect(attrs={'class': ''}),
                'second_hand_yrs': forms.TextInput(attrs={'class': ''}),
                'second_hand_youth': forms.Select(attrs={'class': ''}),
                'second_hand_avg_exposure': forms.TextInput(attrs={'class': ''}),
                'alcohol': forms.RadioSelect(attrs={'class': ''}),
                'alcohol_from_age1': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_to_age1': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_beer1': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_wine1': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_liquor1': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_from_age2': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_to_age2': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_beer2': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_wine2': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_liquor2': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_from_age3': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_to_age3': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_beer3': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_wine3': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_liquor3': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_from_age4': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_to_age4': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_beer4': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_wine4': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_liquor4': forms.TextInput(attrs={'class': ' entry'}),
                'alcohol_current': forms.RadioSelect(attrs={'class': ' entry'}),
                'alcohol_stop_age': forms.TextInput(attrs={'class': ' entry'}),
            }
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     if self.instance:
        #         self.fields['second_hand_leisure'].widget.attrs['checked'] = self.instance.__getattribute__('second_hand_leisure')


class SearchForm(forms.Form):
    class Meta:
        fields = '__all__'





class CT_Scan_Form_Baseline(forms.ModelForm):
    cat_5_findings = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    emphysema_type = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    ct_scan_type_choices = (
        ('Philips', 'Philips'),
        ('Viality', 'Viality'),
    )
    reading_options = (
        ('just CAD', 'just CAD'),
        ('just radiologist', 'just radiologist'),
        ('CAD and radiologist', 'CAD and radiologist'),
    )
    findings_choices = (
        ('normal', 'normal'),
        ('non-actionalbe', 'non-actionalbe'),
        ('actionable', 'actionable'),
    )
    CAT_5_CHOICES = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung Lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    EMPHYSEMA_CHOICES = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    cat_5_findings = forms.MultipleChoiceField(
        choices=CAT_5_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        required=False,
    )
    airways_type = forms.MultipleChoiceField(
        choices=airways_type,
        widget=forms.CheckboxSelectMultiple(attrs={'class': '', 'style': 'checkbox-inline'}),
        required=False,
    )
    class Meta:
        model = ct_scan_baseline
        fields = '__all__'
        widgets = {
        'ct_scan_visitID': forms.HiddenInput(attrs={'class': ''}),
        'ct_scan_location': forms.TextInput(attrs={'class': ''}),
        'ct_scan_guidelines': forms.RadioSelect(attrs={}),
        'ct_scan_guidelines_other': forms.TextInput(attrs={'class': ''}),
        'ct_scan_radiologist': forms.TextInput(attrs={'class': ''}),
        'ct_scan_dlp': forms.TextInput(attrs={'class': ''}),
        'ct_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ct_scan_review_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'finalrec_fu_mnths_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ilst_cat': forms.Select(attrs={'class': ''}),
        'final_rec_fu_mnths': forms.Select(attrs={'class': ''}),
        'fu_completed': forms.RadioSelect(attrs={'class': ''}),
        'actual_fu_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'copd_emphysema': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_extent': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_distribution': forms.RadioSelect(attrs={'class': ''}),
        'airways': forms.RadioSelect(attrs={'class': ''}),
        'airways_type' : forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_findings': forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_comments': forms.Textarea(attrs={'class': '', 'rows': '4'}),
        'other_cardiovascular': forms.RadioSelect(attrs={'class': ''}),
        'other_cardiovascular_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_vertebral': forms.RadioSelect(attrs={'class': ''}),
        'other_vertebral_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_GI': forms.RadioSelect(attrs={'class': ''}),
        'other_GI_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_breast': forms.RadioSelect(attrs={'class': ''}),
        'other_breast_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_endocrine': forms.RadioSelect(attrs={'class': ''}),
        'other_endocrine_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_lymph': forms.RadioSelect(attrs={'class': ''}),
        'other_lymph_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pleura': forms.RadioSelect(attrs={'class': ''}),
        'other_pleura_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pulmonary_fibrosis': forms.RadioSelect(attrs={'class': ''}),
        'other_pulmonary_fibrosis_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_musculoskeletal': forms.RadioSelect(attrs={'class': ''}),
        'other_musculoskeletal_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_other': forms.RadioSelect(attrs={'class': ''}),
        'other_other_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'general_comments': forms.Textarea(attrs={'rows':4}),
    }


class CT_Scan_Form_T1(forms.ModelForm):
    cat_5_findings = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    emphysema_type = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    ct_scan_type_choices = (
        ('Philips', 'Philips'),
        ('Viality', 'Viality'),
    )
    reading_options = (
        ('just CAD', 'just CAD'),
        ('just radiologist', 'just radiologist'),
        ('CAD and radiologist', 'CAD and radiologist'),
    )
    findings_choices = (
        ('normal', 'normal'),
        ('non-actionalbe', 'non-actionalbe'),
        ('actionable', 'actionable'),
    )
    CAT_5_CHOICES = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung Lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    EMPHYSEMA_CHOICES = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    cat_5_findings = forms.MultipleChoiceField(
        choices=CAT_5_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        required=False,
    )
    airways_type = forms.MultipleChoiceField(
        choices=airways_type,
        widget=forms.CheckboxSelectMultiple(attrs={'class': '', 'style': 'checkbox-inline'}),
        required=False,
    )
    class Meta:
        model = ct_scan_t1
        fields = '__all__'
        widgets = {
        'ct_scan_visitID': forms.HiddenInput(attrs={'class': ''}),
        'ct_scan_location': forms.TextInput(attrs={'class': ''}),
        'ct_scan_guidelines': forms.RadioSelect(attrs={}),
        'ct_scan_guidelines_other': forms.TextInput(attrs={'class': ''}),
        'ct_scan_radiologist': forms.TextInput(attrs={'class': ''}),
        'ct_scan_dlp': forms.TextInput(attrs={'class': ''}),
        'ct_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ct_scan_review_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'finalrec_fu_mnths_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ilst_cat': forms.Select(attrs={'class': ''}),
        'final_rec_fu_mnths': forms.Select(attrs={'class': ''}),
        'fu_completed': forms.RadioSelect(attrs={'class': ''}),
        'actual_fu_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'copd_emphysema': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_extent': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_distribution': forms.RadioSelect(attrs={'class': ''}),
        'airways': forms.RadioSelect(attrs={'class': ''}),
        'airways_type' : forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_findings': forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_comments': forms.Textarea(attrs={'class': '', 'rows': '4'}),
        'other_cardiovascular': forms.RadioSelect(attrs={'class': ''}),
        'other_cardiovascular_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_vertebral': forms.RadioSelect(attrs={'class': ''}),
        'other_vertebral_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_GI': forms.RadioSelect(attrs={'class': ''}),
        'other_GI_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_breast': forms.RadioSelect(attrs={'class': ''}),
        'other_breast_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_endocrine': forms.RadioSelect(attrs={'class': ''}),
        'other_endocrine_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_lymph': forms.RadioSelect(attrs={'class': ''}),
        'other_lymph_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pleura': forms.RadioSelect(attrs={'class': ''}),
        'other_pleura_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pulmonary_fibrosis': forms.RadioSelect(attrs={'class': ''}),
        'other_pulmonary_fibrosis_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_musculoskeletal': forms.RadioSelect(attrs={'class': ''}),
        'other_musculoskeletal_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_other': forms.RadioSelect(attrs={'class': ''}),
        'other_other_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'general_comments': forms.Textarea(attrs={'rows':4}),
    }
        
class CT_Scan_Form_T2(forms.ModelForm):
    cat_5_findings = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    emphysema_type = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    ct_scan_type_choices = (
        ('Philips', 'Philips'),
        ('Viality', 'Viality'),
    )
    reading_options = (
        ('just CAD', 'just CAD'),
        ('just radiologist', 'just radiologist'),
        ('CAD and radiologist', 'CAD and radiologist'),
    )
    findings_choices = (
        ('normal', 'normal'),
        ('non-actionalbe', 'non-actionalbe'),
        ('actionable', 'actionable'),
    )
    CAT_5_CHOICES = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung Lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    EMPHYSEMA_CHOICES = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    cat_5_findings = forms.MultipleChoiceField(
        choices=CAT_5_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        required=False,
    )
    airways_type = forms.MultipleChoiceField(
        choices=airways_type,
        widget=forms.CheckboxSelectMultiple(attrs={'class': '', 'style': 'checkbox-inline'}),
        required=False,
    )
    class Meta:
        model = ct_scan_t2
        fields = '__all__'
        widgets = {
        'ct_scan_visitID': forms.HiddenInput(attrs={'class': ''}),
        'ct_scan_location': forms.TextInput(attrs={'class': ''}),
        'ct_scan_guidelines': forms.RadioSelect(attrs={}),
        'ct_scan_guidelines_other': forms.TextInput(attrs={'class': ''}),
        'ct_scan_radiologist': forms.TextInput(attrs={'class': ''}),
        'ct_scan_dlp': forms.TextInput(attrs={'class': ''}),
        'ct_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ct_scan_review_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'finalrec_fu_mnths_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ilst_cat': forms.Select(attrs={'class': ''}),
        'final_rec_fu_mnths': forms.Select(attrs={'class': ''}),
        'fu_completed': forms.RadioSelect(attrs={'class': ''}),
        'actual_fu_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'copd_emphysema': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_extent': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_distribution': forms.RadioSelect(attrs={'class': ''}),
        'airways': forms.RadioSelect(attrs={'class': ''}),
        'airways_type' : forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_findings': forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_comments': forms.Textarea(attrs={'class': '', 'rows': '4'}),
        'other_cardiovascular': forms.RadioSelect(attrs={'class': ''}),
        'other_cardiovascular_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_vertebral': forms.RadioSelect(attrs={'class': ''}),
        'other_vertebral_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_GI': forms.RadioSelect(attrs={'class': ''}),
        'other_GI_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_breast': forms.RadioSelect(attrs={'class': ''}),
        'other_breast_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_endocrine': forms.RadioSelect(attrs={'class': ''}),
        'other_endocrine_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_lymph': forms.RadioSelect(attrs={'class': ''}),
        'other_lymph_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pleura': forms.RadioSelect(attrs={'class': ''}),
        'other_pleura_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pulmonary_fibrosis': forms.RadioSelect(attrs={'class': ''}),
        'other_pulmonary_fibrosis_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_musculoskeletal': forms.RadioSelect(attrs={'class': ''}),
        'other_musculoskeletal_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_other': forms.RadioSelect(attrs={'class': ''}),
        'other_other_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'general_comments': forms.Textarea(attrs={'rows':4}),
    }   

class CT_Scan_Form_T3(forms.ModelForm):
    cat_5_findings = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    emphysema_type = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    ct_scan_type_choices = (
        ('Philips', 'Philips'),
        ('Viality', 'Viality'),
    )
    reading_options = (
        ('just CAD', 'just CAD'),
        ('just radiologist', 'just radiologist'),
        ('CAD and radiologist', 'CAD and radiologist'),
    )
    findings_choices = (
        ('normal', 'normal'),
        ('non-actionalbe', 'non-actionalbe'),
        ('actionable', 'actionable'),
    )
    CAT_5_CHOICES = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung Lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    EMPHYSEMA_CHOICES = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    cat_5_findings = forms.MultipleChoiceField(
        choices=CAT_5_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        required=False,
    )
    airways_type = forms.MultipleChoiceField(
        choices=airways_type,
        widget=forms.CheckboxSelectMultiple(attrs={'class': '', 'style': 'checkbox-inline'}),
        required=False,
    )
    class Meta:
        model = ct_scan_t3
        fields = '__all__'
        widgets = {
        'ct_scan_visitID': forms.HiddenInput(attrs={'class': ''}),
        'ct_scan_location': forms.TextInput(attrs={'class': ''}),
        'ct_scan_guidelines': forms.RadioSelect(attrs={}),
        'ct_scan_guidelines_other': forms.TextInput(attrs={'class': ''}),
        'ct_scan_radiologist': forms.TextInput(attrs={'class': ''}),
        'ct_scan_dlp': forms.TextInput(attrs={'class': ''}),
        'ct_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ct_scan_review_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'finalrec_fu_mnths_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ilst_cat': forms.Select(attrs={'class': ''}),
        'final_rec_fu_mnths': forms.Select(attrs={'class': ''}),
        'fu_completed': forms.RadioSelect(attrs={'class': ''}),
        'actual_fu_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'copd_emphysema': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_extent': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_distribution': forms.RadioSelect(attrs={'class': ''}),
        'airways': forms.RadioSelect(attrs={'class': ''}),
        'airways_type' : forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_findings': forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_comments': forms.Textarea(attrs={'class': '', 'rows': '4'}),
        'other_cardiovascular': forms.RadioSelect(attrs={'class': ''}),
        'other_cardiovascular_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_vertebral': forms.RadioSelect(attrs={'class': ''}),
        'other_vertebral_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_GI': forms.RadioSelect(attrs={'class': ''}),
        'other_GI_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_breast': forms.RadioSelect(attrs={'class': ''}),
        'other_breast_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_endocrine': forms.RadioSelect(attrs={'class': ''}),
        'other_endocrine_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_lymph': forms.RadioSelect(attrs={'class': ''}),
        'other_lymph_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pleura': forms.RadioSelect(attrs={'class': ''}),
        'other_pleura_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pulmonary_fibrosis': forms.RadioSelect(attrs={'class': ''}),
        'other_pulmonary_fibrosis_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_musculoskeletal': forms.RadioSelect(attrs={'class': ''}),
        'other_musculoskeletal_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_other': forms.RadioSelect(attrs={'class': ''}),
        'other_other_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'general_comments': forms.Textarea(attrs={'rows':4}),
    }
      
class CT_Scan_Form_T4(forms.ModelForm):
    cat_5_findings = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    emphysema_type = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    ct_scan_type_choices = (
        ('Philips', 'Philips'),
        ('Viality', 'Viality'),
    )
    reading_options = (
        ('just CAD', 'just CAD'),
        ('just radiologist', 'just radiologist'),
        ('CAD and radiologist', 'CAD and radiologist'),
    )
    findings_choices = (
        ('normal', 'normal'),
        ('non-actionalbe', 'non-actionalbe'),
        ('actionable', 'actionable'),
    )
    CAT_5_CHOICES = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung Lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    EMPHYSEMA_CHOICES = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    cat_5_findings = forms.MultipleChoiceField(
        choices=CAT_5_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        required=False,
    )
    airways_type = forms.MultipleChoiceField(
        choices=airways_type,
        widget=forms.CheckboxSelectMultiple(attrs={'class': '', 'style': 'checkbox-inline'}),
        required=False,
    )
    class Meta:
        model = ct_scan_t4
        fields = '__all__'
        widgets = {
        'ct_scan_visitID': forms.HiddenInput(attrs={'class': ''}),
        'ct_scan_location': forms.TextInput(attrs={'class': ''}),
        'ct_scan_guidelines': forms.RadioSelect(attrs={}),
        'ct_scan_guidelines_other': forms.TextInput(attrs={'class': ''}),
        'ct_scan_radiologist': forms.TextInput(attrs={'class': ''}),
        'ct_scan_dlp': forms.TextInput(attrs={'class': ''}),
        'ct_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ct_scan_review_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'finalrec_fu_mnths_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ilst_cat': forms.Select(attrs={'class': ''}),
        'final_rec_fu_mnths': forms.Select(attrs={'class': ''}),
        'fu_completed': forms.RadioSelect(attrs={'class': ''}),
        'actual_fu_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'copd_emphysema': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_extent': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_distribution': forms.RadioSelect(attrs={'class': ''}),
        'airways': forms.RadioSelect(attrs={'class': ''}),
        'airways_type' : forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_findings': forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_comments': forms.Textarea(attrs={'class': '', 'rows': '4'}),
        'other_cardiovascular': forms.RadioSelect(attrs={'class': ''}),
        'other_cardiovascular_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_vertebral': forms.RadioSelect(attrs={'class': ''}),
        'other_vertebral_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_GI': forms.RadioSelect(attrs={'class': ''}),
        'other_GI_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_breast': forms.RadioSelect(attrs={'class': ''}),
        'other_breast_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_endocrine': forms.RadioSelect(attrs={'class': ''}),
        'other_endocrine_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_lymph': forms.RadioSelect(attrs={'class': ''}),
        'other_lymph_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pleura': forms.RadioSelect(attrs={'class': ''}),
        'other_pleura_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pulmonary_fibrosis': forms.RadioSelect(attrs={'class': ''}),
        'other_pulmonary_fibrosis_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_musculoskeletal': forms.RadioSelect(attrs={'class': ''}),
        'other_musculoskeletal_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_other': forms.RadioSelect(attrs={'class': ''}),
        'other_other_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'general_comments': forms.Textarea(attrs={'rows':4}),
    }
      
class CT_Scan_Form_T5(forms.ModelForm):
    cat_5_findings = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    emphysema_type = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    ct_scan_type_choices = (
        ('Philips', 'Philips'),
        ('Viality', 'Viality'),
    )
    reading_options = (
        ('just CAD', 'just CAD'),
        ('just radiologist', 'just radiologist'),
        ('CAD and radiologist', 'CAD and radiologist'),
    )
    findings_choices = (
        ('normal', 'normal'),
        ('non-actionalbe', 'non-actionalbe'),
        ('actionable', 'actionable'),
    )
    CAT_5_CHOICES = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung Lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    EMPHYSEMA_CHOICES = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    cat_5_findings = forms.MultipleChoiceField(
        choices=CAT_5_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        required=False,
    )
    airways_type = forms.MultipleChoiceField(
        choices=airways_type,
        widget=forms.CheckboxSelectMultiple(attrs={'class': '', 'style': 'checkbox-inline'}),
        required=False,
    )
    class Meta:
        model = ct_scan_t5
        fields = '__all__'
        widgets = {
        'ct_scan_visitID': forms.HiddenInput(attrs={'class': ''}),
        'ct_scan_location': forms.TextInput(attrs={'class': ''}),
        'ct_scan_guidelines': forms.RadioSelect(attrs={}),
        'ct_scan_guidelines_other': forms.TextInput(attrs={'class': ''}),
        'ct_scan_radiologist': forms.TextInput(attrs={'class': ''}),
        'ct_scan_dlp': forms.TextInput(attrs={'class': ''}),
        'ct_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ct_scan_review_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'finalrec_fu_mnths_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ilst_cat': forms.Select(attrs={'class': ''}),
        'final_rec_fu_mnths': forms.Select(attrs={'class': ''}),
        'fu_completed': forms.RadioSelect(attrs={'class': ''}),
        'actual_fu_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'copd_emphysema': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_extent': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_distribution': forms.RadioSelect(attrs={'class': ''}),
        'airways': forms.RadioSelect(attrs={'class': ''}),
        'airways_type' : forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_findings': forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_comments': forms.Textarea(attrs={'class': '', 'rows': '4'}),
        'other_cardiovascular': forms.RadioSelect(attrs={'class': ''}),
        'other_cardiovascular_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_vertebral': forms.RadioSelect(attrs={'class': ''}),
        'other_vertebral_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_GI': forms.RadioSelect(attrs={'class': ''}),
        'other_GI_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_breast': forms.RadioSelect(attrs={'class': ''}),
        'other_breast_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_endocrine': forms.RadioSelect(attrs={'class': ''}),
        'other_endocrine_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_lymph': forms.RadioSelect(attrs={'class': ''}),
        'other_lymph_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pleura': forms.RadioSelect(attrs={'class': ''}),
        'other_pleura_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pulmonary_fibrosis': forms.RadioSelect(attrs={'class': ''}),
        'other_pulmonary_fibrosis_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_musculoskeletal': forms.RadioSelect(attrs={'class': ''}),
        'other_musculoskeletal_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_other': forms.RadioSelect(attrs={'class': ''}),
        'other_other_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'general_comments': forms.Textarea(attrs={'rows':4}),
    }
      
class CT_Scan_Form_T6(forms.ModelForm):
    cat_5_findings = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    emphysema_type = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    ct_scan_type_choices = (
        ('Philips', 'Philips'),
        ('Viality', 'Viality'),
    )
    reading_options = (
        ('just CAD', 'just CAD'),
        ('just radiologist', 'just radiologist'),
        ('CAD and radiologist', 'CAD and radiologist'),
    )
    findings_choices = (
        ('normal', 'normal'),
        ('non-actionalbe', 'non-actionalbe'),
        ('actionable', 'actionable'),
    )
    CAT_5_CHOICES = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung Lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    EMPHYSEMA_CHOICES = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    cat_5_findings = forms.MultipleChoiceField(
        choices=CAT_5_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        required=False,
    )
    airways_type = forms.MultipleChoiceField(
        choices=airways_type,
        widget=forms.CheckboxSelectMultiple(attrs={'class': '', 'style': 'checkbox-inline'}),
        required=False,
    )
    class Meta:
        model = ct_scan_t6
        fields = '__all__'
        widgets = {
        'ct_scan_visitID': forms.HiddenInput(attrs={'class': ''}),
        'ct_scan_location': forms.TextInput(attrs={'class': ''}),
        'ct_scan_guidelines': forms.RadioSelect(attrs={}),
        'ct_scan_guidelines_other': forms.TextInput(attrs={'class': ''}),
        'ct_scan_radiologist': forms.TextInput(attrs={'class': ''}),
        'ct_scan_dlp': forms.TextInput(attrs={'class': ''}),
        'ct_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ct_scan_review_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'finalrec_fu_mnths_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ilst_cat': forms.Select(attrs={'class': ''}),
        'final_rec_fu_mnths': forms.Select(attrs={'class': ''}),
        'fu_completed': forms.RadioSelect(attrs={'class': ''}),
        'actual_fu_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'copd_emphysema': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_extent': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_distribution': forms.RadioSelect(attrs={'class': ''}),
        'airways': forms.RadioSelect(attrs={'class': ''}),
        'airways_type' : forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_findings': forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_comments': forms.Textarea(attrs={'class': '', 'rows': '4'}),
        'other_cardiovascular': forms.RadioSelect(attrs={'class': ''}),
        'other_cardiovascular_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_vertebral': forms.RadioSelect(attrs={'class': ''}),
        'other_vertebral_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_GI': forms.RadioSelect(attrs={'class': ''}),
        'other_GI_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_breast': forms.RadioSelect(attrs={'class': ''}),
        'other_breast_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_endocrine': forms.RadioSelect(attrs={'class': ''}),
        'other_endocrine_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_lymph': forms.RadioSelect(attrs={'class': ''}),
        'other_lymph_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pleura': forms.RadioSelect(attrs={'class': ''}),
        'other_pleura_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pulmonary_fibrosis': forms.RadioSelect(attrs={'class': ''}),
        'other_pulmonary_fibrosis_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_musculoskeletal': forms.RadioSelect(attrs={'class': ''}),
        'other_musculoskeletal_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_other': forms.RadioSelect(attrs={'class': ''}),
        'other_other_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'general_comments': forms.Textarea(attrs={'rows':4}),
    }
      
class CT_Scan_Form_T7(forms.ModelForm):
    cat_5_findings = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    emphysema_type = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    ct_scan_type_choices = (
        ('Philips', 'Philips'),
        ('Viality', 'Viality'),
    )
    reading_options = (
        ('just CAD', 'just CAD'),
        ('just radiologist', 'just radiologist'),
        ('CAD and radiologist', 'CAD and radiologist'),
    )
    findings_choices = (
        ('normal', 'normal'),
        ('non-actionalbe', 'non-actionalbe'),
        ('actionable', 'actionable'),
    )
    CAT_5_CHOICES = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung Lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]
    EMPHYSEMA_CHOICES = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
    cat_5_findings = forms.MultipleChoiceField(
        choices=CAT_5_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        required=False,
    )
    airways_type = forms.MultipleChoiceField(
        choices=airways_type,
        widget=forms.CheckboxSelectMultiple(attrs={'class': '', 'style': 'checkbox-inline'}),
        required=False,
    )
    class Meta:
        model = ct_scan_t7
        fields = '__all__'
        widgets = {
        'ct_scan_visitID': forms.HiddenInput(attrs={'class': ''}),
        'ct_scan_location': forms.TextInput(attrs={'class': ''}),
        'ct_scan_guidelines': forms.RadioSelect(attrs={}),
        'ct_scan_guidelines_other': forms.TextInput(attrs={'class': ''}),
        'ct_scan_radiologist': forms.TextInput(attrs={'class': ''}),
        'ct_scan_dlp': forms.TextInput(attrs={'class': ''}),
        'ct_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ct_scan_review_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'finalrec_fu_mnths_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ilst_cat': forms.Select(attrs={'class': ''}),
        'final_rec_fu_mnths': forms.Select(attrs={'class': ''}),
        'fu_completed': forms.RadioSelect(attrs={'class': ''}),
        'actual_fu_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'copd_emphysema': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_extent': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'copd_emphysema_distribution': forms.RadioSelect(attrs={'class': ''}),
        'airways': forms.RadioSelect(attrs={'class': ''}),
        'airways_type' : forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_findings': forms.CheckboxSelectMultiple(attrs={'class': ''}),
        'cat_5_comments': forms.Textarea(attrs={'class': '', 'rows': '4'}),
        'other_cardiovascular': forms.RadioSelect(attrs={'class': ''}),
        'other_cardiovascular_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_vertebral': forms.RadioSelect(attrs={'class': ''}),
        'other_vertebral_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_GI': forms.RadioSelect(attrs={'class': ''}),
        'other_GI_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_breast': forms.RadioSelect(attrs={'class': ''}),
        'other_breast_comments': forms.Textarea(attrs={'rows': 4, 'class': ''}),
        'other_endocrine': forms.RadioSelect(attrs={'class': ''}),
        'other_endocrine_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_lymph': forms.RadioSelect(attrs={'class': ''}),
        'other_lymph_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pleura': forms.RadioSelect(attrs={'class': ''}),
        'other_pleura_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_pulmonary_fibrosis': forms.RadioSelect(attrs={'class': ''}),
        'other_pulmonary_fibrosis_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_musculoskeletal': forms.RadioSelect(attrs={'class': ''}),
        'other_musculoskeletal_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'other_other': forms.RadioSelect(attrs={'class': ''}),
        'other_other_comments': forms.Textarea(attrs={'rows': 4,'class': ''}),
        'general_comments': forms.Textarea(attrs={'rows':4}),
    }
      
class CT_Scan_Nodule_Form_1(ModelForm):
    class Meta:
        model = ct_scan_nodule_1
        fields = '__all__'
        widgets = {
            'nodule_rank': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_slice_num': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_status': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_radiologist_accepted': forms.RadioSelect(attrs={}),
            'nodule_technition_accepted': forms.RadioSelect(attrs={}),
            'nodule_interval_change': forms.RadioSelect(attrs={}),
            'nodule_location_selection' : forms.RadioSelect(attrs={}),
            'nodule_type': forms.RadioSelect(attrs={}),
            'nodule_axis_long': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_short': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_mean': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_long': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_short': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_description': forms.Select(attrs={}),
            'nodule_location': forms.RadioSelect(attrs={}),
            'nodule_comments': forms.Textarea(attrs={'rows': '2'}),
            'nodule_risk_index': forms.RadioSelect(),
            'nodule_key_nodule': forms.CheckboxInput(attrs={}),
            'nodule_cancer_confirmed': forms.CheckboxInput(attrs={}),
            'nodule_recommended_fu': forms.Select(attrs={}),
            'nodule_orders': forms.TextInput(attrs={}),
            'nodule_status_cad': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_interval_change_cad': forms.RadioSelect(attrs={}),
            'nodule_location_selection_cad' : forms.RadioSelect(attrs={}),
            'nodule_type_cad': forms.RadioSelect(attrs={}),
            'nodule_axis_long_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_short_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_mean_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_volume_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_density_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_sd_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_long_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_short_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_description_cad': forms.Select(attrs={}),
            'nodule_location_cad': forms.RadioSelect(attrs={}),
            'nodule_volume_doubling_time_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_change_volume_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_mean_diam_change_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_comments_cad': forms.Textarea(attrs={'rows': '2'}),
            'nodule_key_nodule_cad': forms.CheckboxInput(attrs={}),
            'nodule_cancer_confirmed_cad': forms.CheckboxInput(attrs={}),
            'nodule_recommended_fu_cad': forms.Select(attrs={}),
        }

class CT_Scan_Nodule_Form_2(ModelForm):
    class Meta:
        model = ct_scan_nodule_2
        fields = '__all__'
        widgets = {
            'nodule_rank': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_slice_num': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_status': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_radiologist_accepted': forms.RadioSelect(attrs={}),
            'nodule_technition_accepted': forms.RadioSelect(attrs={}),
            'nodule_interval_change': forms.RadioSelect(attrs={}),
            'nodule_location_selection' : forms.RadioSelect(attrs={}),
            'nodule_type': forms.RadioSelect(attrs={}),
            'nodule_axis_long': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_short': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_mean': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_long': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_short': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_description': forms.Select(attrs={}),
            'nodule_location': forms.RadioSelect(attrs={}),
            'nodule_comments': forms.Textarea(attrs={'rows': '2'}),
            'nodule_risk_index': forms.RadioSelect(),
            'nodule_key_nodule': forms.CheckboxInput(attrs={}),
            'nodule_cancer_confirmed': forms.CheckboxInput(attrs={}),
            'nodule_recommended_fu': forms.Select(attrs={}),
            'nodule_orders': forms.TextInput(attrs={}),
            'nodule_status_cad': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_interval_change_cad': forms.RadioSelect(attrs={}),
            'nodule_location_selection_cad' : forms.RadioSelect(attrs={}),
            'nodule_type_cad': forms.RadioSelect(attrs={}),
            'nodule_axis_long_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_short_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_mean_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_volume_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_density_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_sd_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_long_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_short_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_description_cad': forms.Select(attrs={}),
            'nodule_location_cad': forms.RadioSelect(attrs={}),
            'nodule_volume_doubling_time_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_change_volume_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_mean_diam_change_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_comments_cad': forms.Textarea(attrs={'rows': '2'}),
            'nodule_key_nodule_cad': forms.CheckboxInput(attrs={}),
            'nodule_cancer_confirmed_cad': forms.CheckboxInput(attrs={}),
            'nodule_recommended_fu_cad': forms.Select(attrs={}),
        }

class CT_Scan_Nodule_Form_3(ModelForm):
    class Meta:
        model = ct_scan_nodule_3
        fields = '__all__'
        widgets = {
            'nodule_rank': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_slice_num': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_status': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_radiologist_accepted': forms.RadioSelect(attrs={}),
            'nodule_technition_accepted': forms.RadioSelect(attrs={}),
            'nodule_interval_change': forms.RadioSelect(attrs={}),
            'nodule_location_selection' : forms.RadioSelect(attrs={}),
            'nodule_type': forms.RadioSelect(attrs={}),
            'nodule_axis_long': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_short': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_mean': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_long': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_short': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_description': forms.Select(attrs={}),
            'nodule_location': forms.RadioSelect(attrs={}),
            'nodule_comments': forms.Textarea(attrs={'rows': '2'}),
            'nodule_risk_index': forms.RadioSelect(),
            'nodule_key_nodule': forms.CheckboxInput(attrs={}),
            'nodule_cancer_confirmed': forms.CheckboxInput(attrs={}),
            'nodule_recommended_fu': forms.Select(attrs={}),
            'nodule_orders': forms.TextInput(attrs={}),
            'nodule_status_cad': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_interval_change_cad': forms.RadioSelect(attrs={}),
            'nodule_location_selection_cad' : forms.RadioSelect(attrs={}),
            'nodule_type_cad': forms.RadioSelect(attrs={}),
            'nodule_axis_long_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_short_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_mean_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_volume_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_density_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_sd_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_long_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_short_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_description_cad': forms.Select(attrs={}),
            'nodule_location_cad': forms.RadioSelect(attrs={}),
            'nodule_volume_doubling_time_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_change_volume_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_mean_diam_change_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_comments_cad': forms.Textarea(attrs={'rows': '2'}),
            'nodule_key_nodule_cad': forms.CheckboxInput(attrs={}),
            'nodule_cancer_confirmed_cad': forms.CheckboxInput(attrs={}),
            'nodule_recommended_fu_cad': forms.Select(attrs={}),
        }

class CT_Scan_Nodule_Form_4(ModelForm):
    class Meta:
        model = ct_scan_nodule_4
        fields = '__all__'
        widgets = {
            'nodule_rank': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_slice_num': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_status': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_radiologist_accepted': forms.RadioSelect(attrs={}),
            'nodule_technition_accepted': forms.RadioSelect(attrs={}),
            'nodule_interval_change': forms.RadioSelect(attrs={}),
            'nodule_location_selection' : forms.RadioSelect(attrs={}),
            'nodule_type': forms.RadioSelect(attrs={}),
            'nodule_axis_long': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_short': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_mean': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_long': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_short': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_description': forms.Select(attrs={}),
            'nodule_location': forms.RadioSelect(attrs={}),
            'nodule_comments': forms.Textarea(attrs={'rows': '2'}),
            'nodule_risk_index': forms.RadioSelect(),
            'nodule_key_nodule': forms.CheckboxInput(attrs={}),
            'nodule_cancer_confirmed': forms.CheckboxInput(attrs={}),
            'nodule_recommended_fu': forms.Select(attrs={}),
            'nodule_orders': forms.TextInput(attrs={}),
            'nodule_status_cad': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_interval_change_cad': forms.RadioSelect(attrs={}),
            'nodule_location_selection_cad' : forms.RadioSelect(attrs={}),
            'nodule_type_cad': forms.RadioSelect(attrs={}),
            'nodule_axis_long_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_short_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_mean_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_volume_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_density_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_sd_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_long_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_short_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_description_cad': forms.Select(attrs={}),
            'nodule_location_cad': forms.RadioSelect(attrs={}),
            'nodule_volume_doubling_time_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_change_volume_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_mean_diam_change_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_comments_cad': forms.Textarea(attrs={'rows': '2'}),
            'nodule_key_nodule_cad': forms.CheckboxInput(attrs={}),
            'nodule_cancer_confirmed_cad': forms.CheckboxInput(attrs={}),
            'nodule_recommended_fu_cad': forms.Select(attrs={}),
        }

class CT_Scan_Nodule_Form_5(ModelForm):
    class Meta:
        model = ct_scan_nodule_5
        fields = '__all__'
        widgets = {
            'nodule_rank': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_slice_num': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_status': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_radiologist_accepted': forms.RadioSelect(attrs={}),
            'nodule_technition_accepted': forms.RadioSelect(attrs={}),
            'nodule_interval_change': forms.RadioSelect(attrs={}),
            'nodule_location_selection' : forms.RadioSelect(attrs={}),
            'nodule_type': forms.RadioSelect(attrs={}),
            'nodule_axis_long': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_short': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_mean': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_long': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_short': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_description': forms.Select(attrs={}),
            'nodule_location': forms.RadioSelect(attrs={}),
            'nodule_comments': forms.Textarea(attrs={'rows': '2'}),
            'nodule_risk_index': forms.RadioSelect(),
            'nodule_key_nodule': forms.CheckboxInput(attrs={}),
            'nodule_cancer_confirmed': forms.CheckboxInput(attrs={}),
            'nodule_recommended_fu': forms.Select(attrs={}),
            'nodule_orders': forms.TextInput(attrs={}),
            'nodule_status_cad': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_interval_change_cad': forms.RadioSelect(attrs={}),
            'nodule_location_selection_cad' : forms.RadioSelect(attrs={}),
            'nodule_type_cad': forms.RadioSelect(attrs={}),
            'nodule_axis_long_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_short_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_mean_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_volume_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_density_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_axis_sd_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_long_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_ssn_short_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_description_cad': forms.Select(attrs={}),
            'nodule_location_cad': forms.RadioSelect(attrs={}),
            'nodule_volume_doubling_time_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_change_volume_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_mean_diam_change_cad': forms.TextInput(attrs={'class': 'form-control-xs'}),
            'nodule_comments_cad': forms.Textarea(attrs={'rows': '2'}),
            'nodule_key_nodule_cad': forms.CheckboxInput(attrs={}),
            'nodule_cancer_confirmed_cad': forms.CheckboxInput(attrs={}),
            'nodule_recommended_fu_cad': forms.Select(attrs={}),
        }

class inclusion_form(ModelForm):
    YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No'),
    ]
    inclusion_criteria_1 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_2 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_3 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_4 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_5 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_6 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_7 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_8 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_9 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )


    

    class Meta:  
        model = inclusion
        fields = '__all__'
        widgets = {
      
        'inclusion_criteria_1': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'inclusion_criteria_2': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'inclusion_criteria_3': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'inclusion_criteria_4': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'inclusion_criteria_5': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'inclusion_criteria_6': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'inclusion_criteria_7': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'inclusion_criteria_8': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'inclusion_criteria_9': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'inclusion_status': forms.Select(attrs={'class': ''}),
        'screening_status': forms.Select(attrs={'class': ''}),
        'consent_status': forms.Select(attrs={'class': ''}),
        'consent_form': forms.FileInput(attrs={'class': ''}),
        'consent_form_path': forms.TextInput(attrs={'disabled': 'disabled'}),
        'parpticpant_status' : forms.Select(attrs={'class': ''}),
        'comments' : forms.Textarea(attrs={'class' : ''}),

        }



class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'participant_number': forms.TextInput(),  
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participant_number'].required = False 

class plco_score_form(forms.ModelForm):
    YES_NO_CHOICES = [
    (1, 'Yes'),
    (0, 'No'),
    ]   
    copd = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        coerce=lambda x: x == 'True'
    )
    cancer_history = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        coerce=lambda x: x == 'True'
    )
    lung_cancer_history = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        coerce=lambda x: x == 'True'
    )
    smoking_status = forms.TypedChoiceField(
        choices=[
            (1, 'Current'),
            (0, 'Former'),
        ],
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
        coerce=lambda x: x == 'True'
    )
    EDUCATION_CHOICES = [
        ('Less than high school graduate', 'Less than high school graduate'),
        ('High school graduate', 'High school graduate'),
        ('Post high school training', 'Post high school training'),
        ('Some college', 'Some college'),
        ('College graduate', 'College graduate'),
        ('Postgraduate', 'Postgraduate'),
    ]
    education = forms.ChoiceField(
        choices=EDUCATION_CHOICES,
        widget=forms.Select(attrs={'class': ''})
    )
    class Meta:
        model = PLCO_score
        fields = '__all__'
        widgets = { 
        'participant_num': forms.TextInput(attrs={'class': ''}),
        'age': forms.NumberInput(attrs={'class': ''}),
        'bmi': forms.NumberInput(attrs={'class': ''}),
        'copd': forms.TextInput(attrs={'class': ''}),
        'cancer_history': forms.TextInput(attrs={'class': ''}),
        'lung_cancer_history': forms.TextInput(attrs={'class': ''}),
        'race': forms.Select(attrs={'class': ''}),
        'smoking_status': forms.TextInput(attrs={'class': ''}),
        'avg_num_cigs_smoked_day': forms.NumberInput(attrs={'class': ''}),
        'duration_smoked': forms.NumberInput(attrs={'class': ''}),
        'years_quit': forms.NumberInput(attrs={'class': ''}),
    }




class ParticipantSearchForm(forms.Form):
    participant_number = forms.CharField(label='Participant Number')



class annual_study_update_part_a_form(forms.Form):

    Model = annual_study_update_part_a
    fields = '__all__'
    widgets = {
        'update_starting_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'update_end_sate': forms.TextInput(attrs={'maxlength': 20}),
        'followup_time_period': forms.Select(choices=annual_study_update_part_a.time_period_choices),
        'regular_family_doc': forms.CheckboxInput(),
        'gp_name': forms.TextInput(attrs={'maxlength': 20}),
        'gp_address': forms.TextInput(attrs={'maxlength': 20}),
        'gp_telephone': forms.TextInput(attrs={'maxlength': 20}),
        'gp_msp': forms.TextInput(attrs={'maxlength': 20}),
        'gp_fax': forms.TextInput(attrs={'maxlength': 20}),
        'gp_visit': forms.CheckboxInput(),
        'chest_xray': forms.CheckboxInput(),
        'chest_xray_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ct_scan_chest': forms.CheckboxInput(),
        'ct_scan_chest_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'ct_scan_heart': forms.CheckboxInput(),
        'ct_scan_heart_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'chest_mri': forms.CheckboxInput(),
        'chest_mri_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'pet_scan': forms.CheckboxInput(),
        'pet_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'nuclear_scan': forms.CheckboxInput(),
        'nuclear_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'surgery_chest_lung': forms.CheckboxInput(),
        'surgery_chest_lung_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'biopsy_chest_lung': forms.CheckboxInput(),
        'biopsy_chest_lung_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'bronchoscopy': forms.CheckboxInput(),
        'bronchoscopy_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'lung_cancer_chemo': forms.CheckboxInput(),
        'lung_cancer_chemo_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'lung_cancer_radiation': forms.CheckboxInput(),
        'lung_cancer_radiation_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'other_lung_cancer_treatment': forms.CheckboxInput(),
        'other_lung_cancer_treatment_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'other_lung_cancer_treatment_info': forms.TextInput(attrs={'maxlength': 20}),
        'other_medical_procedures': forms.CheckboxInput(),
        'other_medical_procedures_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'other_medical_procedures_info': forms.TextInput(attrs={'maxlength': 20}),
        'lung_cancer_diagnosis': forms.CheckboxInput(),
        'lung_cancer_diagnosis_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'lung_cancer_diagnosis_info': forms.TextInput(attrs={'maxlength': 20}),
        'lung_cancer_treatment': forms.CheckboxInput(),
        'lung_cancer_treatment_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'lung_cancer_treatment_info': forms.TextInput(attrs={'maxlength': 20}),
        'lung_chest_care': forms.CheckboxInput(),
        'lung_chest_care_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'lung_chest_care_info': forms.TextInput(attrs={'maxlength': 20}),
        'other_cancer_diagnosis': forms.CheckboxInput(),
        'other_cancer_diagnosis_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'other_cancer_diagnosis_info': forms.TextInput(attrs={'maxlength': 20}),
        'other_condition_diagnosis': forms.CheckboxInput(),
        'other_condition_diagnosis_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'other_condition_diagnosis_info': forms.TextInput(attrs={'maxlength': 20}),
        'heart_disease_heat_attack': forms.CheckboxInput(),
        'heart_disease_heat_attack_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'heart_disease_heart_info': forms.TextInput(attrs={'maxlength': 20}),
        'high_cholesterol': forms.CheckboxInput(),
        'high_cholestrol_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'high_cholerstrol_info': forms.TextInput(attrs={'maxlength': 20}),
        'new_meds_cholestrol': forms.CheckboxInput(),
        'new_meds_cholestrol_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'new_meds_cholestrol_info': forms.TextInput(attrs={'maxlength': 20}),
    }


class annual_study_update_part_b_form(forms.ModelForm):
    YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No'),
    ]
    smoked_past_12_months = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    current_smoker = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    reduced_cigs_per_day = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    fam_doc_cig_smoking = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    fam_doc_stop_smoking = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    fam_doc_nic_replacement = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    fam_doc_counselling = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    fam_doc_fuvisit = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_nic_replacement = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_zyban = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_champix = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_ecigs = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_cessation_program = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_smoke_councellor = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_quit_24hrs = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )






    class Meta:
        model = annual_study_update_part_b
        fields = '__all__'
        widgets = {
            'smoked_past_12_months': forms.CheckboxInput(),
            'smoked_past_12_months_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'current_smoker': forms.CheckboxInput(),
            'cigs_per_day': forms.TextInput(attrs={'maxlength': 20}),
            'cigs_per_day_amount': forms.TextInput(attrs={'maxlength': 20}),
            'reduced_cigs_per_day': forms.CheckboxInput(),
            'fam_doc_cig_smoking': forms.CheckboxInput(),
            'fam_doc_stop_smoking': forms.CheckboxInput(),
            'fam_doc_nic_replacement': forms.CheckboxInput(),
            'fam_doc_counselling': forms.CheckboxInput(),
            'fam_doc_fuvisit': forms.CheckboxInput(),
            'past_yr_nic_replacement': forms.Select(choices=annual_study_update_part_b.nic_replacement),
            'past_yr_zyban': forms.CheckboxInput(),
            'past_yr_champix': forms.CheckboxInput(),
            'past_yr_ecigs': forms.CheckboxInput(),
            'past_yr_ecigs_nic': forms.Select(choices=annual_study_update_part_b.nic),
            'past_yr_cessation_program': forms.CheckboxInput(),
            'past_yr_cessation_program_study': forms.TextInput(attrs={'maxlength': 20}),
            'past_yr_smoke_councellor': forms.CheckboxInput(),
            'past_yr_smoke_councellor_info': forms.TextInput(attrs={'maxlength': 20}),
            'past_yr_quit_24hrs': forms.CheckboxInput(),
            'past_yr_quit_24hrs_length': forms.NumberInput(),
            'completed_form': forms.Select(choices=annual_study_update_part_b.person),
            'person_assisted': forms.TextInput(attrs={'maxlength': 20}),
            'person_assisted_other': forms.TextInput(attrs={'maxlength': 20}),
            'date_completed': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'checked_by': forms.TextInput(attrs={'maxlength': 20}),
            'checked_by_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        }


class annual_study_update_medications_form(forms.Form):
    Model = annual_study_update_medications
    fields = '__all__'
    widgets = {
        'medication_name': forms.TextInput(attrs={'maxlength': 20}),
        'medication_dose': forms.TextInput(attrs={'maxlength': 20}),
        'medication_frequency': forms.TextInput(attrs={'maxlength': 20}),
        'medication_reason': forms.TextInput(attrs={'maxlength': 20}),
        'medication_start_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
        'medication_last_taken': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
    }
    


class annual_study_update_form(forms.ModelForm):

    YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No'),
    ]
    smoked_past_12_months = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    current_smoker = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    reduced_cigs_per_day = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    fam_doc_cig_smoking = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    fam_doc_stop_smoking = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    fam_doc_nic_replacement = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    fam_doc_counselling = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    fam_doc_fuvisit = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_zyban = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_champix = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_ecigs = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_cessation_program = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_smoke_councellor = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    past_yr_quit_24hrs = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    chest_xray = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    ct_scan_chest = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    ct_scan_heart = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    chest_mri = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    pet_scan = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    nuclear_scan = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    surgery_chest_lung = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    biopsy_chest_lung = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    bronchoscopy = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    lung_cancer_chemo = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    lung_cancer_radiation = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    other_lung_cancer_treatment = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    other_medical_procedures = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    lung_cancer_diagnosis = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    lung_cancer_treatment = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    lung_chest_care = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    other_cancer_diagnosis = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    other_condition_diagnosis = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    heart_disease_heat_attack = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    high_cholesterol = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    new_meds_cholestrol = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    class Meta:
        model = annual_study_update
        fields = '__all__'
        widgets = {
            'medication_name': forms.TextInput(attrs={'maxlength': 20}),
            'medication_dose': forms.TextInput(attrs={'maxlength': 20}),
            'medication_frequency': forms.TextInput(attrs={'maxlength': 20}),
            'medication_reason': forms.TextInput(attrs={'maxlength': 20}),
            'medication_start_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'medication_last_taken': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'smoked_past_12_months': forms.CheckboxInput(),
            'smoked_past_12_months_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'current_smoker': forms.CheckboxInput(),
            'cigs_per_day': forms.TextInput(attrs={'maxlength': 20}),
            'cigs_per_day_amount': forms.TextInput(attrs={'maxlength': 20}),
            'reduced_cigs_per_day': forms.CheckboxInput(),
            'fam_doc_cig_smoking': forms.CheckboxInput(),
            'fam_doc_stop_smoking': forms.CheckboxInput(),
            'fam_doc_nic_replacement': forms.CheckboxInput(),
            'fam_doc_counselling': forms.CheckboxInput(),
            'fam_doc_fuvisit': forms.CheckboxInput(),
            'past_yr_nic_replacement': forms.Select(),
            'past_yr_zyban': forms.CheckboxInput(),
            'past_yr_champix': forms.CheckboxInput(),
            'past_yr_ecigs': forms.CheckboxInput(),
            'past_yr_ecigs_nic': forms.Select(choices=annual_study_update_part_b.nic),
            'past_yr_cessation_program': forms.CheckboxInput(),
            'past_yr_cessation_program_study': forms.TextInput(attrs={'maxlength': 20}),
            'past_yr_smoke_councellor': forms.CheckboxInput(),
            'past_yr_smoke_councellor_info': forms.TextInput(attrs={'maxlength': 20}),
            'past_yr_quit_24hrs': forms.CheckboxInput(),
            'past_yr_quit_24hrs_length': forms.NumberInput(),
            'completed_form': forms.Select(choices=annual_study_update_part_b.person),
            'person_assisted': forms.TextInput(attrs={'maxlength': 20}),
            'person_assisted_other': forms.TextInput(attrs={'maxlength': 20}),
            'date_completed': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'checked_by': forms.TextInput(attrs={'maxlength': 20}),
            'checked_by_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'update_starting_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'update_end_sate': forms.TextInput(attrs={'maxlength': 20}),
            'followup_time_period': forms.Select(choices=annual_study_update_part_a.time_period_choices),
            'regular_family_doc': forms.CheckboxInput(),
            'gp_name': forms.TextInput(attrs={'maxlength': 20}),
            'gp_address': forms.TextInput(attrs={'maxlength': 20}),
            'gp_telephone': forms.TextInput(attrs={'maxlength': 20}),
            'gp_msp': forms.TextInput(attrs={'maxlength': 20}),
            'gp_fax': forms.TextInput(attrs={'maxlength': 20}),
            'gp_visit': forms.CheckboxInput(),
            'chest_xray': forms.CheckboxInput(),
            'chest_xray_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'ct_scan_chest': forms.CheckboxInput(),
            'ct_scan_chest_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'ct_scan_heart': forms.CheckboxInput(),
            'ct_scan_heart_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'chest_mri': forms.CheckboxInput(),
            'chest_mri_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'pet_scan': forms.CheckboxInput(),
            'pet_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'nuclear_scan': forms.CheckboxInput(),
            'nuclear_scan_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'surgery_chest_lung': forms.CheckboxInput(),
            'surgery_chest_lung_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'biopsy_chest_lung': forms.CheckboxInput(),
            'biopsy_chest_lung_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'bronchoscopy': forms.CheckboxInput(),
            'bronchoscopy_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'lung_cancer_chemo': forms.CheckboxInput(),
            'lung_cancer_chemo_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'lung_cancer_radiation': forms.CheckboxInput(),
            'lung_cancer_radiation_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'other_lung_cancer_treatment': forms.CheckboxInput(),
            'other_lung_cancer_treatment_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'other_lung_cancer_treatment_info': forms.TextInput(attrs={'maxlength': 20}),
            'other_medical_procedures': forms.CheckboxInput(),
            'other_medical_procedures_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'other_medical_procedures_info': forms.TextInput(attrs={'maxlength': 20}),
            'lung_cancer_diagnosis': forms.CheckboxInput(),
            'lung_cancer_diagnosis_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'lung_cancer_diagnosis_info': forms.TextInput(attrs={'maxlength': 20}),
            'lung_cancer_treatment': forms.CheckboxInput(),
            'lung_cancer_treatment_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'lung_cancer_treatment_info': forms.TextInput(attrs={'maxlength': 20}),
            'lung_chest_care': forms.CheckboxInput(),
            'lung_chest_care_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'lung_chest_care_info': forms.TextInput(attrs={'maxlength': 20}),
            'other_cancer_diagnosis': forms.CheckboxInput(),
            'other_cancer_diagnosis_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'other_cancer_diagnosis_info': forms.TextInput(attrs={'maxlength': 20}),
            'other_condition_diagnosis': forms.CheckboxInput(),
            'other_condition_diagnosis_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'other_condition_diagnosis_info': forms.TextInput(attrs={'maxlength': 20}),
            'heart_disease_heat_attack': forms.CheckboxInput(),
            'heart_disease_heat_attack_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'heart_disease_heart_info': forms.TextInput(attrs={'maxlength': 20}),
            'high_cholesterol': forms.CheckboxInput(),
            'high_cholestrol_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'high_cholerstrol_info': forms.TextInput(attrs={'maxlength': 20}),
            'new_meds_cholestrol': forms.CheckboxInput(),
            'new_meds_cholestrol_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'new_meds_cholestrol_info': forms.TextInput(attrs={'maxlength': 20}),
    }
        
class ProtocolDeviationsForm(forms.ModelForm):
    class Meta:
        model = Protocol_Deviations
        exclude = ('id',)
        fields = '__all__'
        widgets = {
            'participant_num': forms.HiddenInput(attrs={'class': 'hidden'}),
            'date_of_deviation': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'type_of_deviation': forms.Select(attrs={'class': ''}),
            'description_of_deviation': forms.Textarea(attrs={'class': ''}),
        }

class clinical_procedures_form(forms.ModelForm):
    class Meta:
        model = Clinical_Procedures
        exclude = ('id',)
        fields = '__all__'
        widgets = {
            'participant_num': forms.HiddenInput(attrs={'class': 'hidden'}),
            'procedure_date': forms.DateInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'procedure_type': forms.Textarea(attrs={'rows': 3, 'class': ''}),
            'procedure_pdf': forms.FileInput(attrs={'class': ''}),
      
        }



from .models import pdf_uploads_questionnaire

class pdf_uploads_questionnaire_form(forms.ModelForm):
    class Meta:
        model = pdf_uploads_questionnaire
        fields = '__all__'



class PdfUploadForm(forms.Form):
    document = forms.FileField(label='Select a file')


from .models import UploadedPDF

class UploadPDFForm(forms.ModelForm):
    class Meta:
        model = UploadedPDF
        fields = ['pdf_file']