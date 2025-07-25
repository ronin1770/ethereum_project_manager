
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Sprint
from .forms import ProjectForm, SprintForm
from contracts.project_contract import push_project_to_chain
from contracts.sprint_contract import push_sprint_to_chain


# === Project Views ===

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'blockchain_sprint_manager/project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'blockchain_sprint_manager/project_detail.html', {'project': project})


def project_create(request):
    """if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'blockchain_sprint_manager/project_form.html', {'form': form})"""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()  # This saves and returns the instance
            try:
                tx_hash = push_project_to_chain(project)
                print(f"✅ Project pushed to blockchain: {tx_hash}")
            except Exception as e:
                print(f"⚠️ Blockchain push failed: {e}")
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'blockchain_sprint_manager/project_form.html', {'form': form})


# === Sprint Views ===

def sprint_list(request):
    sprints = Sprint.objects.all()
    return render(request, 'blockchain_sprint_manager/sprint_list.html', {'sprints': sprints})


def sprint_detail(request, pk):
    sprint = get_object_or_404(Sprint, pk=pk)
    return render(request, 'blockchain_sprint_manager/sprint_detail.html', {'sprint': sprint})


def sprint_create(request):
    """if request.method == 'POST':
        form = SprintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sprint_list')
    else:
        form = SprintForm()
    return render(request, 'blockchain_sprint_manager/sprint_form.html', {'form': form})"""
    if request.method == 'POST':
        form = SprintForm(request.POST)
        if form.is_valid():
            sprint = form.save()  # Save the Sprint instance
            try:
                tx_hash = push_sprint_to_chain(sprint)
                print(f"✅ Sprint pushed to blockchain: {tx_hash}")
            except Exception as e:
                print(f"⚠️ Blockchain push failed: {e}")
            return redirect('sprint_list')
    else:
        form = SprintForm()
    return render(request, 'blockchain_sprint_manager/sprint_form.html', {'form': form})



def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'blockchain_sprint_manager/dashboard.html', {'projects': projects})
