# TrashScanner Infrastructure 🚀🐳

[![Deploy Infrastructure](https://github.com/trashscanner/trashscanner_infra/actions/workflows/deploy-infrastructure.yml/badge.svg)](https://github.com/trashscanner/trashscanner_infra/actions/workflows/deploy-infrastructure.yml)
[![Check Status](https://github.com/trashscanner/trashscanner_infra/actions/workflows/check-status.yml/badge.svg)](https://github.com/trashscanner/trashscanner_infra/actions/workflows/check-status.yml)
[![License](https://img.shields.io/github/license/trashscanner/trashscanner_infra)](https://github.com/trashscanner/trashscanner_infra/blob/master/LICENSE)

Автоматизированное развертывание инфраструктуры для проекта TrashScanner. Управляет развертыванием PostgreSQL и MinIO на удаленном сервере через GitHub Actions и Ansible.

## 🎯 Назначение

Этот репозиторий содержит конфигурацию для автоматического развертывания базовой инфраструктуры TrashScanner:

- **PostgreSQL 16** - основная база данных приложения
- **MinIO** - S3-совместимое объектное хранилище для изображений отходов

Развертывание выполняется одной кнопкой через GitHub Actions с использованием Ansible для настройки и управления Docker контейнерами.

## 📄 Лицензия

Apache-2.0

---

Сделано с ❤️ для заботы об экологии
