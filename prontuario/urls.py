from django.urls import path
from prontuario.views import DadosMedicosUpdate, MedicamentosUpdate, SaudeUpdate, ExameFisicoIBUpdate, \
    PlanoTratamentoUpdate, CondOclusalUpadate, OdontogramaUpadate, PSRUpadate, ProcedimentoUpdate

urlpatterns = [
    path("dados-med-edit/<int:pk>/", DadosMedicosUpdate.as_view(), name="dados_med_edit"),
    path("med-edit/<int:pk>/", MedicamentosUpdate.as_view(), name="med_edit"),
    path("sau-edit/<int:pk>/", SaudeUpdate.as_view(), name="sau_edit"),
    path("exam-fis-ib-edit/<int:pk>/", ExameFisicoIBUpdate.as_view(), name="exam_edit"),
    path("plan-edit/<int:pk>/", PlanoTratamentoUpdate.as_view(), name="plan_edit"),
    path("cond-edit/<int:pk>/", CondOclusalUpadate.as_view(), name="cond_edit"),
    path("odon-edit/<int:pk>/", OdontogramaUpadate.as_view(), name="odon_edit"),
    path("psr-edit/<int:pk>/", PSRUpadate.as_view(), name="psr_edit"),
    path("proc-edit/<int:pk>/", ProcedimentoUpdate.as_view(), name="proc_edit"),

]
