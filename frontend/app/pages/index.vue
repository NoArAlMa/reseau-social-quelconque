<script lang="ts" setup>
import type { ButtonProps, PageFeatureProps } from "@nuxt/ui";

const { $t } = useI18n();

useHead(() => ({
  title: String($t("seo.welcomeTitle")),
  htmlAttrs: {
    class: "scroll-smooth",
  },
  meta: [
    {
      name: "NohamDrive | Welcome Page",
      content: String($t("seo.welcomeDescription")),
    },
  ],
}));

useSeoMeta({
  description: String($t("seo.welcomeDescription")),
  ogTitle: String($t("seo.welcomeTitle")),
  ogDescription: String($t("seo.welcomeDescription")),
  ogImage: "[og:image]",
  ogUrl: "[og:url]",
  twitterTitle: String($t("seo.welcomeTitle")),
  twitterDescription: String($t("seo.welcomeDescription")),
  twitterImage: "[twitter:image]",
  twitterCard: "summary",
});
definePageMeta({
  layout: "welcome",
  middleware: "app-middleware",
});

const { isMobile } = useResponsive();

const features = computed(() => [
  {
    title: String($t("welcome.cards.advancedExplorer.title")),
    description: String($t("welcome.cards.advancedExplorer.description")),
    icon: "material-symbols:folder",
  },
  {
    title: String($t("welcome.cards.secureSharing.title")),
    description: String($t("welcome.cards.secureSharing.description")),
    icon: "material-symbols:share",
  },
  {
    title: String($t("welcome.cards.openSource.title")),
    description: String($t("welcome.cards.openSource.description")),
    icon: "material-symbols:code-rounded",
  },
]);

const pageSection: PageFeatureProps[] = [
  {
    title: $t("welcome.sections.terminalEcho.title") as string,
    description: $t("welcome.sections.terminalEcho.description") as string,
    icon: "terminal:echo-icon",
  },
  {
    title: $t("welcome.sections.realtimeCollab.title") as string,
    description: $t("welcome.sections.realtimeCollab.description") as string,
    icon: "material-symbols:group-outline-rounded",
  },
  {
    title: $t("welcome.sections.security.title") as string,
    description: $t("welcome.sections.security.description") as string,
    icon: "material-symbols:lock-outline",
  },
];

const links = computed<ButtonProps[]>(() => [
  {
    label: $t("common.getStarted") as string,
    to: "/auth",
    icon: "material-symbols:play-arrow-outline-rounded",
  },
  {
    label: $t("common.learnMore") as string,
    to: "#features",
    color: "neutral",
    variant: "subtle",
    trailingIcon: "material-symbols:arrow-forward-rounded",
  },
]);

const PageTitle = computed(() => String($t("welcome.heroTitle")));
const PageDesc = computed(() => String($t("welcome.heroDesc")));
</script>

<template>
  <section class="flex flex-col">
    <div class="min-h-screen">
      <UPageSection
        :features="pageSection"
        :title="PageTitle"
        :description="PageDesc"
        :links="links"
        class="mb-10"
      />

      <div id="features" class="py-16 px-4 sm:py-20 sm:px-6 lg:py-24 lg:px-8">
        <div class="max-w-7xl mx-auto">
          <h2
            v-if="isMobile"
            class="text-3xl sm:text-4xl md:text-5xl font-bold text-center mb-12 md:mb-16"
          >
            {{ $t("welcome.featuresHeadingMobile") }}
          </h2>
          <UPageGrid
            class="grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8"
          >
            <UPageCard
              v-for="(card, index) in features"
              :key="index"
              v-bind="card"
              :ui="{
                title: 'mb-3',
              }"
              class="h-full hover:shadow-lg transition-all duration-300 hover:transform hover:-translate-y-1"
            />
          </UPageGrid>
        </div>
      </div>
    </div>
    <div
      id="echo"
      class="min-h-[80vh] w-full flex flex-col rounded-md md:flex-row items-center justify-center gap-12 px-4 sm:px-8 py-12 bg-gray-200 dark:bg-gray-800"
    >
      <div class="flex-1 max-w-md text-center md:text-left">
        <h1
          class="text-5xl sm:text-5xl font-bold flex items-center justify-center md:justify-start gap-3 mb-6"
        >
          {{ $t("welcome.echoHeading") }}
          <UIcon name="terminal:echo-icon" class="text-primary" dynamic />
        </h1>
        <p class="text-lg sm:text-x mb-8 max-w-lg">
          {{ $t("welcome.echoLead") }}
          <span class="font-semibold">{{ $t("welcome.echoLeadStrong") }}</span>
        </p>
        <UButton
          :label="String($t('common.learnMore'))"
          color="primary"
          variant="solid"
          size="lg"
          class="mx-auto md:mx-0"
          icon="material-symbols:arrow-forward-rounded"
        />
      </div>

      <div
        class="flex-1 max-w-none md:max-w-2xl lg:max-w-3xl xl:max-w-4xl relative"
      >
        <div class="relative rounded-xl overflow-hidden shadow-2xl">
          <img
            class="w-full h-auto rounded-xl"
            style="max-width: 100%; height: auto; aspect-ratio: 16/9"
            src="/images/echo.png"
          ></img>
        </div>
      </div>
    </div>
  </section>
</template>
